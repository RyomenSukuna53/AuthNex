from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import random
import asyncio
from pyrogram.handlers import MessageHandler
from config import * 
from AuthNex import app as AuthNex 
from AuthNex.Database import user_col


# Reset command function
async def reset_handler(_, m: Message):
    bars = [
    "▱▱▱▱▱▱▱▱▱▱  0%",
    "▰▱▱▱▱▱▱▱▱▱ 10%",
    "▰▰▱▱▱▱▱▱▱▱ 20%",
    "▰▰▰▱▱▱▱▱▱▱ 30%",
    "▰▰▰▰▱▱▱▱▱▱ 40%",
    "▰▰▰▰▰▱▱▱▱▱ 50%",
    "▰▰▰▰▰▰▱▱▱▱ 60%",
    "▰▰▰▰▰▰▰▱▱▱ 70%",
    "▰▰▰▰▰▰▰▰▱▱ 80%",
    "▰▰▰▰▰▰▰▰▰▱ 90%",
    "▰▰▰▰▰▰▰▰▰▰ 100%"
    ]
    
    data = await user_col.find({})
    if not data:
        await m.reply_text("🧐") 
        await asyncio.sleep(1) 
        await m.delete() 
        await m.reply("😕 𝙽𝚘 𝚕𝚘𝚐𝚒𝚗𝚜 𝚏𝚘𝚞𝚗𝚍 𝚒𝚗 𝚏𝚒𝚕𝚎𝚜 📁") 
        return 

    await m.reply("🧐") 
    await asyncio.sleep(1) 
    await m.delete() 
    sync = await m.reply("Deleting...") 

    for bar in bars:
        await sync.edit_text(f"```shell\n𝔻𝔼𝕃𝔼𝕋𝕀ℕ𝔾...\n{bar}```", parse_mode=ParseMode.MARKDOWN) 
        await asyncio.sleep(1)

    # Optionally delete the data
    await user_col.delete({})

    await sync.edit_text(
        f"𝔸𝕝𝕝 𝔻𝕠𝕟𝕖. 𝔸𝕝𝕝 𝔻𝕒𝕥𝕒𝕓𝕒𝕤𝕖 𝕗𝕚𝕝𝕖𝕤 𝕒𝕣𝕖 𝕕𝕖𝕝𝕖𝕥𝕖𝕕.\n{bars[-1]}"
    )

# Proper handler (with correct filters)
ResetHandlerObject = MessageHandler(
    reset_handler,
    filters.command("reset") & (filters.private | filters.group) & filters.user(SUDO)
)

# Add this to your main.py file:
# app.add_handler(reset_handler_obj)

