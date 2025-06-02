from AuthNex import app as AuthNex 
from pyrogram import filters 
from pyrogram.enums import ParseMode 
from AuthNex.Bars import Bars 
from pyrogram.types import Message 
from pyrogram.handlers import MessageHandler
import asyncio as AsyncIO 
from config import SUDO
from AuthNex.Database import user_col as User

async def reset(_, m: Message):
    # Check if any user exists
    if not User.find_one({}):
        await m.reply_text("🧐") 
        await AsyncIO.sleep(1) 
        await m.delete() 
        await m.reply("😕 𝙽𝚘 𝚕𝚘𝚐𝚒𝚗𝚜 𝚏𝚘𝚞𝚗𝚍 𝚒𝚗 𝚏𝚒𝚕𝚎𝚜 📁") 
        return 

    await m.reply("🧐") 
    await AsyncIO.sleep(1) 
    sync = await m.reply("Deleting...") 
    
    last_bar = ""
    for bar in Bars:
        await sync.edit_text(f"```shell\n𝔻𝔼𝕃𝔼𝕋𝕀ℕ𝔾...\n{bar}```", parse_mode=ParseMode.MARKDOWN)
        last_bar = bar
        await AsyncIO.sleep(1)

    # Drop user data (you can replace this with User.delete_many({}) or proper cleanup)
    User.delete_many({})

    await sync.edit_text(f"✅ 𝔸𝕝𝕝 𝔻𝕠𝕟𝕖. 𝔻𝕒𝕥𝕒 𝕓𝕒𝕤𝕖 𝕗𝕚𝕝𝕖𝕤 𝕒𝕣𝕖 𝕔𝕝𝕖𝕒𝕣.\n{last_bar}")

# Register handler
reset_handler = MessageHandler(
    reset, 
    filters.command('reset') & (filters.group | filters.private) & filters.user(SUDO)
)


