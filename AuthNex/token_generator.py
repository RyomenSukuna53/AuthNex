from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
import secrets
import asyncio

from AuthNex import app
from AuthNex.Database import user_col, sessions_col, tokens_col

async def generate_authnex_token(length=50):
    return secrets.token_hex(length // 2)  # generates a secure token

@Client.on_message(filters.command("generatetoken") & filters.private, group=14)
async def token_generator(_, message: Message):
    user_id = message.from_user.id

    # Ensure command is used only in private chat
    if message.chat.type != ChatType.PRIVATE:
        return await message.reply("❌ Use this command in **private chat only.**")

    session = await sessions_col.find_one({"_id": user_id})
    if not session:
        return await message.reply("❌ You must be logged in to generate a token.")

    mail = session.get("mail")
    user = await user_col.find_one({"Mail": mail})
    if not user:
        return await message.reply("⚠️ User record not found.")

    # Check if token already exists
    existing_token = await tokens_col.find_one({"id": user_id})
    if existing_token:
        return await message.reply("✅ You already have a token.\nUse `/revoketoken` to regenerate.")

    # Ask for password
    await message.reply("🔐 Please send your **password** to confirm token generation.")

    if message.text != mail:
        return
    await message.reply("🔑Generating... ")
    await asyncio.sleep(1)
    await message.delete()
    token = await generate_authnex_token()
    await message.reply(f" ✅ Token: `{token}`")
    await tokens_col.insert_one({"_id": user_id,
                                 "token": token})
