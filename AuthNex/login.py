from pyrogram import Client, filters
from pyrogram.types import Message
import datetime
from AuthNex.Database import user_col, sessions_col
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

    # Step 1: Mail
    if state["step"] == "mail":
        state["mail"] = text
        state["step"] = "password"
        await message.reply("🔐 Enter your **password**:")

    # Step 2: Password
    elif state["step"] == "password":
        mail = state["mail"]
        password = text

        user = await user_col.find_one({"Mail": mail, "Password": password})
        if not user:
            await message.reply("❌ Invalid mail or password.")
            del login_state[user_id]
            return

        # Send OTP
        code = await authentication_code(mail, user_id)  # <-- Sends code to user via bot
        state["otp"] = code
        state["step"] = "otp"
        await message.reply("✅ Mail & password verified.\n\n📨 Enter the **OTP** sent to your Telegram account.")

    # Step 3: OTP
    elif state["step"] == "otp":
        entered_code = text
        expected_code = state.get("otp")

        if entered_code != expected_code:
            await message.reply("❌ Incorrect OTP. Login failed.")
            del login_state[user_id]
            return

        # Save session
        await sessions_col.insert_one({
            "_id": user_id,
            "mail": state["mail"],
            "login_time": datetime.datetime.utcnow()
        })

        await message.reply("✅ Login successful. Welcome!")
        del login_state[user_id]
