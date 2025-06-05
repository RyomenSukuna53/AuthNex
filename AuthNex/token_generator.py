from pyrogram import Client, filters
from pyrogram.types import Message
from AuthNex.__init__ import app
from AuthNex.Database import user_col, sessions_col, ban_col, tokens_col
import secrets
from asyncio import sleep
from pyrogram.enums import ChatType, ParseMode
import asyncio

async def generate_authnex_token(length=50):
    return secrets.token_hex(length // 2)  # length in hex digits


@Client.on_message(filters.command("generatetoken") & filters.private, group=13)
async def token_generator(Client, message: Message):
    user = message.from_user
    user_id = user.id

    if message.chat.type == ChatType.GROUP:
        return await message.reply("USE IN DM")
    session = await sessions_col.find_one({"_id": user_id})
    mail = session.get('mail')
    user = user_col.find_one({"Mail": mail})
    if not session:
        return
    token = await tokens_col.find_one({"_id": user_id})
    if token:
        return
    while True:
        token = await generate_authnex_token()
        if tokens_col.find_one({"token": token}):
            break
    await message.reply("•--> 𝗘𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝘁𝗼 𝗰𝗼𝗻𝗳𝗶𝗿𝗺")
    password = message.text
    if password != user.get('Password'):
        return await message.reply("Wrong pass try again after some time.")
    await message.reply("🔑 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐓𝐨𝐤𝐞𝐧...")
    await asyncio.sleep(1)
    await message.delete()
    await message.reply(f"𝗬𝗼𝘂𝗿 𝗧𝗢𝗞𝗘𝗡: `{token}`\nUse this to use 𝔸𝗨𝗧𝗛ℕ𝗘𝕏 codes and library.")
    await tokens_col.insert_one({"id": user_id,
                                 "token": token
                                })
