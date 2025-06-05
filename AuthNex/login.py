from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import datetime
from AuthNex import app
from AuthNex.Database import user_col, sessions_col
from AuthNex.Modules.auth import authentication_code

login_state = {}
pending_login = {}

@app.on_message(filters.command('login') & filters.private, group=8)
async def start_login(_, message: Message):
    user_id = message.from_user.id
    session = await sessions_col.find_one({"_id": user_id})
    if session:
        return await message.reply(f"❌ You're already logged in as `{session.get('mail')}`.\nUse `/logout` first.")
    
    login_state[user_id] = {"step": "mail"}
    await message.reply("📧 Please enter your **mail** to login:")

@app.on_message(filters.text & filters.private)
async def handle_login_input(_, message: Message):
    user_id = message.from_user.id
    if user_id not in login_state:
        return

    state = login_state[user_id]
    text = message.text.strip()

    if state["step"] == "mail":
        state["mail"] = text
        state["step"] = "password"
        await message.reply("🔐 Enter your **password**:")

    elif state["step"] == "password":
        mail = state["mail"]
        password = text

        user = await user_col.find_one({"Mail": mail, "Password": password})
        if not user:
            await message.reply("❌ Invalid mail or password.")
            del login_state[user_id]
            return

        session = await sessions_col.find_one({"mail": mail})

        if not session:
            await sessions_col.insert_one({
                "_id": user_id,
                "mail": mail,
                "login_time": datetime.datetime.utcnow()
            })
            await message.reply(f"✅ Logged in directly as `{user.get('Name')}` (no active session found).")
            del login_state[user_id]
            return

        old_user_id = session["_id"]
        code = await authentication_code(mail, old_user_id)
        state["otp"] = code
        state["step"] = "otp"

        # Send approval request to old session user
        pending_login[mail] = {
            "new_user_id": user_id,
            "new_user_name": message.from_user.first_name,
            "mail": mail,
            "user_name": user.get("Name")
        }

        try:
            await app.send_message(
                chat_id=old_user_id,
                text=f"⚠️ Someone is trying to login to your account: **{user.get('Name')}**\nDo you want to allow it?",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("✅ Yes, it's safe", callback_data=f"allow_login:{mail}")],
                    [InlineKeyboardButton("❌ Terminate", callback_data=f"terminate_login:{mail}")]
                ])
            )
            await message.reply("📨 Login detected from another device.\nWaiting for the owner to approve...")
        except:
            await message.reply("❌ Couldn't contact the owner session. Try again later.")
            del login_state[user_id]

    elif state["step"] == "otp":
        if text != state.get("otp"):
            await message.reply("❌ Incorrect OTP. Login denied.")
            del login_state[user_id]
            return

        await sessions_col.insert_one({
            "_id": user_id,
            "mail": state["mail"],
            "login_time": datetime.datetime.utcnow()
        })
        await message.reply("✅ OTP verified! You're now logged in.")
        del login_state[user_id]


@app.on_callback_query(filters.regex("^(allow_login|terminate_login):"))
async def handle_login_decision(_, query: CallbackQuery):
    action, mail = query.data.split(":")
    info = pending_login.get(mail)

    if not info:
        return await query.answer("⚠️ This session is no longer pending.", show_alert=True)

    new_id = info["new_user_id"]
    old_id = query.from_user.id
    name = info["user_name"]

    if action == "allow_login":
        await sessions_col.insert_one({
            "_id": new_id,
            "mail": mail,
            "login_time": datetime.datetime.utcnow()
        })

        await app.send_message(new_id, f"✅ Login approved by owner. You're now logged in as `{name}`.")
        await query.edit_message_text("✅ Login request allowed.")
        del pending_login[mail]
        login_state.pop(new_id, None)

    elif action == "terminate_login":
        await sessions_col.delete_one({"mail": mail})
        await sessions_col.insert_one({
            "_id": new_id,
            "mail": mail,
            "login_time": datetime.datetime.utcnow()
        })

        await app.send_message(old_id, "❌ Your session was terminated by the account owner.")
        await app.send_message(new_id, f"✅ Login approved. Old session terminated. You're now logged in as `{name}`.")
        await query.edit_message_text("⚠️ Old session terminated. New login active.")
        del pending_login[mail]
        login_state.pop(new_id, None)
