import io
from pyrogram import *

from AuthNex import AuthNex as bot

import traceback

from subprocess import getoutput as run

from pyrogram.enums import ChatAction

from pyrogram.types import Message 

from pyrogram.handlers import MessageHandler

async def logs(_, message: Message):
    if message.from_user.id == 6239769036:
      run_logs = run("tail log.txt")
      text = await message.reply_text("`Getting logs...`")
      await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
      await message.reply_text(f"```shell\n{run_logs}```")
      await text.delete()
    else: 
      return

logs = MessageHandler(logs, filters.command("logs") & (filters.private | filters.group)) 




