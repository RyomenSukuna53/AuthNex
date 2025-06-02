from AuthNex import app as AuthNex 
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from AuthNex import app as AuthNex 
from AuthNex.Database import user_col
import random
import asyncio as AsyncIO
from pyrogram.handlers import MessageHandler
from config import * 
from AuthNex.Bars import Bars


# Reset command function
async def reset_handler(_, m: Message):
    user_id = m.from_user.id

    # Check if database has any data
    data = User.find({})
    if not data:
        await m.reply_text("🧐") 
        await AsyncIO.sleep(1) 
        await m.delete() 
        await m.reply("😕 𝙽𝚘 𝚕𝚘𝚐𝚒𝚗𝚜 𝚏𝚘𝚞𝚗𝚍 𝚒𝚗 𝚏𝚒𝚕𝚎𝚜 📁") 
        return 

    await m.reply("🧐") 
    await AsyncIO.sleep(1) 
    sync = await m.reply("Deleting...") 

    for bar in Bars:
        await sync.edit_text(f"```shell\n𝔻𝔼𝕃𝔼𝕋𝕀ℕ𝔾...\n{bar}```", parse_mode=ParseMode.MARKDOWN) 
        await AsyncIO.sleep(1)

    # Optionally delete the data
    User.delete({})

    await sync.edit_text(
        f"𝔸𝕝𝕝 𝔻𝕠𝕟𝕖. 𝔸𝕝𝕝 𝔻𝕒𝕥𝕒𝕓𝕒𝕤𝕖 𝕗𝕚𝕝𝕖𝕤 𝕒𝕣𝕖 𝕕𝕖𝕝𝕖𝕥𝕖𝕕.\n{Bars[-1]}"
    )

# Proper handler (with correct filters)
ResetHandlerObject = MessageHandler(
    reset_handler,
    filters.command("reset") & (filters.private | filters.group) & filters.user(SUDO)
)

# Add this to your main.py file:
# app.add_handler(reset_handler_obj)

