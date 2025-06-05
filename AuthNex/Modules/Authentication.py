import random
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType, ParseMode
from AuthNex.Modules import HelperBot

async def code_generator(_, m: Message):
    code = random.randint(10000, 99999)
    _id = m.from_user.id
    await Client.send_message(chat_id=_id, text=`"Your Authentication Code: {code}`")
