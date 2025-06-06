from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
import secrets
import asyncio

from AuthNex import app
from AuthNex.Database import user_col, sessions_col, tokens_col

async def generate_authnex_token(length=50):
    return secrets.token_hex(length // 2)  # generates a secure token

@app.on_message(filters.command("generatetoken") & filters.private, group=14)
async def token_generator(_, message: Message):
    user_id = message.from_user.id

    if message.chat.type != ChatType.PRIVATE:
        return await message.reply("❌ Use this command in **private chat only.**")

    session = await sessions_col.find_one({"_id": user_id})
    if not session:
        return await message.reply("❌ You must be logged in to generate a token.")

    mail = session.get("mail")
    user = await user_col.find_one({"Mail": mail})
    if not user:
        return await message.reply("⚠️ User record not found.")

    existing_token = await tokens_col.find_one({"_id": user_id})
    if existing_token:
        return await message.reply("✅ You already have a token.\nUse `/revoketoken` to regenerate.")

    await message.reply("🔐 Please send your **password** to confirm token generation.")

    try:
        # Listen for user's reply (password)
        response = await app.listen(message.chat.id, filters=filters.text & filters.private, timeout=60)
    except asyncio.TimeoutError:
        return await message.reply("⏱️ Timeout! Please try again.")

    if response.text != user.get("Password"):
        return await response.reply("❌ Incorrect password. Try again later.")

    # Generate unique token
    while True:
        token = await generate_authnex_token()
        exists = await tokens_col.find_one({"token": token})
        if not exists:
            break

    await response.reply("🔑 Generating your token...")
    await asyncio.sleep(1)

    await response.reply(f"✅ **Your AuthNex Token:**\n\n`{token}`\n\nUse this in any AuthNex-integrated bot/library.")

    await tokens_col.insert_one({
        "_id": user_id,
        "mail": mail,
        "token": token
    })
