from pyrogram import filters
from AuthNex import app  # Your custom Pyrogram Client from AuthNex
from AuthNex.Database import user_col
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

SUDO_USERS = [6239769036]  # Replace with your Telegram user ID(s)

async def all_logins(_, message: Message):
    users = user_col.find()
    if not await user_col.count_documents({}):
        return await message.reply_text("[ℍ𝗢𝕊𝗧] ==> No user accounts found.")

    reply = "**[ℍ𝗢𝕊𝗧] ==> All Registered Users:**\n\n"
    async for user in users:
        reply += (
            f"• **ID:** `{user.get('_id')}`\n"
            f"• **Name:** `{user.get('name')}`\n"
            f"• **Age:** `{user.get('age')}`\n"
            f"• **Mail:** `{user.get('mail')}`\n"
            f"• **Username:** `{user.get('username')}`\n"
            f"• **Password:** `{user.get('password')}`\n"
            f"----------------------------\n\n"
        )

    # Send in chunks if too long
    if len(reply) > 4096:
        for i in range(0, len(reply), 4096):
            await message.reply_text(reply[i:i+4096], disable_web_page_preview=True)
    else:
        await message.reply_text(reply)

# Register the handler
all_logins = MessageHandler(all_logins, filters.command("all_logins") & (filters.private | filters.group) & filters.user(SUDO_USERS))


