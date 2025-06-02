from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from AuthNex import app
from AuthNex.Database import user_col
import random
import asyncio
from pyrogram.handlers import MessageHandler

SUDO_USER = [6239769036]

async def accounts(_, m: Message):
    users = user_col.find_many({"_id": None}) 

    if not user:
      await m.reply("😭")
      await m.reply("𝗡𝗼 𝗜𝗗'𝗦 𝗳𝗼𝘂𝗻𝗱.") 
      return 

    reply = "🗝 𝗔𝗹𝗹 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝘂𝘀𝗲𝗿𝘀 𝗹𝗶𝘀𝘁 💳\n\n"
    for user in users:
      reply += f"**𝗡𝗔𝗠𝗘:** {user.get('Name')}\n"
             f"**AGE:** {user.get('Age')}\n"
             f"**𝗔𝗨𝗧𝗛-𝗠𝗔𝗜𝗟:** {user.get('Mail')}\n" 
             f"**𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗:** {user.get('Password')}\n" 
             f"**ID:** {user.get('_id')}\n"
             f"**AUTH-COINS:** {user.get('Authcoins')}\n"
             f"**OWNER:** {user.get('Owner')}\n\n"
             "----------------------------------\n\n"

    await m.reply(reply) 

accounts = MessageHandler(accounts, filters.command('accounts') & (filters.group | filters.private) & filters.user(SUDO_USER)) 
