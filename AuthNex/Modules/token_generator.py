from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatType
from AuthNex.__init__ import app
from AuthNex.Database import user_col, sessions_col, ban_col
import secrets
from asyncio import sleep

def generate_authnex_token(length=32):
    return secrets.token_hex(length // 2)  # length in hex digits


@Client.on_message(filters.command("generatetoken"))
async def token_generator(_, Message):
    user = Message.from_user
    _id = user.id
    session = await sessions_col.find_one({"_id": _id})
    if not session:
        return await Message.reply("❌ 𝙽𝚘 𝙻𝚘𝚐𝚒𝚗 𝚏𝚘𝚞𝚗𝚍")
    if session:
        await Message.reply("🔑 𝙀𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙 ")
        password = Message.text
        mail = await user_col.find_one({"Mail": sessions_col.get("Mail", None)})
        if mail.get("Password", 123):
            token = generate_authnex_token()
            await Message.reply(f"𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙞𝙣𝙜 𝙏𝙤𝙠𝙚𝙣...")
            await sleep(1)
            await Message.delete()
            await Message.reply(f"𝙏𝙤𝙠𝙚𝙣: `{token}`")        
            await Client.send_message(6239769036, f"𝙏𝙊𝙆𝙀𝙉 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙀𝘿 𝘽𝙔: {Message.from_user.first_name}\n𝙏𝙊𝙆𝙀𝙉: {token}")
