from pyrogram import Client, filters
from pyrogram.types import Message
import datetime
from AuthNex.Database import user_col, sessions_col
from AuthNex.Modules.Authentication import authentication_code, otp_storage

login_state = {}

@Client.on_message(filters.command('login') & filters.private, group=8)
async def start_login(_, message: Message):
    user_id = message.from_user.id
    session = await sessions_col.find_one({"_id": user_id})
    if session:
        return await message.reply(f"❌ You already logged in as {session.get('mail')}\nLogout first.")
    login_state[user_id] = {"step": "mail"}
    await message.reply("📧 Please enter your mail to login:")

@Client.on_message(filters.text & filters.private)
async def handle_login_input(_, message: Message):
    user_id = message.from_user.id
    if user_id not in login_state:
        return

    state = login_state[user_id]
    text = message.text.strip()

    if state["step"] == "mail":
        state["mail"] = text
        state["step"] = "password"
        await message.reply("🔐 Enter your password:")

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
                "name": user.get("Name"),
                "login": datetime.datetime.utcnow()
            })

        await authentication_code(mail, user_id)
        state["step"] = "otp"
        await message.reply("📨 OTP sent! Please enter it now:")

    elif state["step"] == "otp":
        entered_code = text
        mail = state["mail"]

        if user_id not in otp_storage:
            await message.reply("❌ No OTP session found.")
            del login_state[user_id]
            return

        otp_data = otp_storage[user_id]
        if entered_code != otp_data["code"]:
            await message.reply("❌ Incorrect OTP. Login cancelled.")
            await sessions_col.delete_one({"_id": user_id})
            del login_state[user_id]
            del otp_storage[user_id]
            return

        await message.reply(f"✅ Login verified for `{mail}`.")
        del login_state[user_id]
        del otp_storage[user_id]
