from pyrogram import Client, filters
from pyrogram.types import Message
import datetime
from AuthNex.Database import user_col, sessions_col
from AuthNex import app
from AuthNex.Modules.auth import authentication_code, otp_storage

login_state = {}

@Client.on_message(filters.command('login') & filters.private, group=8)
async def start_login(_, message: Message):
    user_id = message.from_user.id
    session = await sessions_col.find_one({"_id": user_id})
    if session:
        return await message.reply(f"❌ You're already logged in as `{session.get('mail')}`.\nUse `/logout` first.")
    
    login_state[user_id] = {"step": "mail"}
    await message.reply("📧 Please enter your **mail** to login:")

@Client.on_message(filters.text & filters.private)
async def handle_login_input(_, message: Message):
    user_id = message.from_user.id
    if user_id not in login_state:
        return

    state = login_state[user_id]
    text = message.text.strip()

    # Step 1: Enter Mail
    if state["step"] == "mail":
        state["mail"] = text
        state["step"] = "password"
        await message.reply("🔐 Enter your **password**:")

    # Step 2: Enter Password
    elif state["step"] == "password":
        mail = state["mail"]
        password = text

        user = await user_col.find_one({"Mail": mail, "Password": password})
        if not user:
            await message.reply("❌ Invalid mail or password.")
            del login_state[user_id]
            return

        # Check if someone is already logged in with this mail
        existing_session = await sessions_col.find_one({"mail": mail})

        if not existing_session:
            # No one logged in => Direct login
            await sessions_col.insert_one({
                "_id": user_id,
                "mail": mail,
                "login_time": datetime.datetime.utcnow()
            })

            await message.reply(f"✅ Logged in directly as `{user.get('Name')}` (no active session found).")
            del login_state[user_id]
            return

        # Someone is already logged in, ask OTP
        code = await authentication_code(mail, existing_session.get("_id"))
        state["otp"] = code
        state["step"] = "otp"
        await message.reply("📨 Someone is already logged in with this mail.\nEnter the **OTP** sent to your Telegram account.")

    # Step 3: OTP Check
    elif state["step"] == "otp":
        entered = text
        expected = state.get("otp")

        if entered != expected:
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
