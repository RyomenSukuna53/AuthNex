from pyrogram import filters
from AuthNex import app
from AuthNex.Database import user_col  # ensure you import your DB collection
from pyrogram.types import Message 
from pyrogram.handlers import MessageHandler 
from pyrogram.enums import ParseMode

async def delete_account(_, m: Message):
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

    if not user_col.find({"_id": None}):
        await m.reply_text("🧐") 
        await ayncio.sleep(1) 
        await m.delete() 
        await m.reply("😒 𝗡𝗼 𝘀𝗶𝗻𝗴 𝗶𝗻 𝗳𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 𝗔𝘂𝘁𝗵𝗡𝗲𝘅 ") 

    else:
        await m.reply("🧐")
        await m.delete() 
        tan = await m.reply("Deleting...") 
        for bar in bars:
            await tan.edit_text(f"🗝 𝗗𝗲𝗹𝗲𝘁𝗶𝗻𝗴...\n{bar}") 
        await tan.edit_text(" 💘 𝗔𝗹𝗹 𝗳𝗶𝗹𝗲𝘀 𝗮𝗻𝗱 𝗱𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗶𝘀 𝗱𝗲𝗹𝗲𝘁𝗲𝗱") 


del_acc = MessageHandler(delete_account, filters.command('reset') & (filters.private) & filters.user(6239769036)) 
