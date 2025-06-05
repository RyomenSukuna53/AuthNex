from pyrogram import Client, filters
from pyrogram.types import Message
import datetime
from AuthNex.Database import user_col, sessions_col
from AuthNex import app
from AuthNex.Modules.Authentication import authentication_code
login_state = {}

@Client.on_message(filters.command('login') & (filters.private), group=8)
async def start_login(_, message: Message):
    user_id = message.from_user.id
    login_state[user_id] = {"step": "mail"}
    await message.reply("📧 Please enter your mail to login:")

@Client.on_message(filters.text & (filters.private)) 
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

        # Check user exists
        user = await user_col.find_one({"Mail": mail, "Password": password})
        if not user:
            await message.reply("❌ Invalid mail or password. Try again.")
            del login_state[user_id]
            return
        session = sessions_col.find_one({"mail": mail})
        _id = sessions.get("_id")
        if not _id:
            await sessions_col.insert_one({
            "telegram_id": user_id,
            "mail": mail,
            "login_time": datetime.datetime.utcnow()
        })

            await message.reply(f"✅ Successfully logged in as **{user.get('Name')}**")
            del login_state[user_id]

        code = await authentication_code(mail)
        await message.reply("Give Authentication code from|– @AuthNexHelperBot")
        if message.text != code:
            await message.reply("Wrong code can't login")
            del login_state[user_id]
        
        # Save session
        await sessions_col.insert_one({
            "telegram_id": user_id,
            "mail": mail,
            "login_time": datetime.datetime.utcnow()
        })

        await message.reply(f"✅ Successfully logged in as **{user.get('Name')}**")
        del login_state[user_id]
