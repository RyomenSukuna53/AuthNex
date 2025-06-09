from pyrogram import Client, filters
from pyrogram.types import Message
from AuthNex import app
from AuthNex.Database import sessions_col
from config import SUDO

@Client.on_message(filters.command["broadcast", "bcast"] & filters.private & filters.user(SUDO), group=26)
async def broadcast_by_KURORAIJIN(_, m: Message):
    users = await user_col.find_many({"_id": None})
    msg = m.text[1:]
    await m.reply("BROADCAST STARTED...")
    for user in users:
        await Client.send_message(user, msg)
