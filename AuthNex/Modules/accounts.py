from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from AuthNex.Database import user_col
from AuthNex import app

SUDO_USER = [6239769036]

async def accounts_handler(_, m: Message):
    users = user_col.find({})  # Fetch all users

    # Check if users exist
    if not await user_col.count_documents({}):
        await m.reply("😭")
        await m.reply("𝗡𝗼 𝗜𝗗'𝗦 𝗳𝗼𝘂𝗻𝗱.") 
        return 

    reply = "🗝 𝗔𝗹𝗹 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿𝘀 𝗹𝗶𝘀𝘁 💳\n\n"
    for user in users:
        reply += (
            f"**𝗡𝗔𝗠𝗘:** {user.get('Name', 'N/A')}\n"
            f"**AGE:** {user.get('Age', 'N/A')}\n"
            f"**𝗔𝗨𝗧𝗛-𝗠𝗔𝗜𝗟:** {user.get('Mail', 'N/A')}\n" 
            f"**𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗:** {user.get('Password', 'N/A')}\n" 
            f"**ID:** {user.get('_id', 'N/A')}\n"
            f"**AUTH-COINS:** {user.get('Authcoins', 'N/A')}\n"
            f"**LOGINED:** {user.get('Login')}\n"
            f"**OWNER:** {user.get('Owner', 'N/A')}\n\n"
            "----------------------------------\n\n"
        )

    await m.reply(reply, quote=True)

accounts_handler_obj = MessageHandler(accounts_handler, filters.command('accounts') & (filters.group | filters.private) & filters.user(SUDO_USER)
)

# Don't forget to add this in your main file:
# app.add_handler(accounts_handler_obj)

