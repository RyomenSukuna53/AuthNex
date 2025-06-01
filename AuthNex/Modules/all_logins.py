from pyrogram import filters
from AuthNex import app  # Your custom Pyrogram Client from AuthNex
from AuthNex.Database import user_col
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler


async def all_logins(_, m: Message):
    users = await user_col.find("_id": None)
    if not await user_col.count_documents({}):
        return await m.reply_text("[ℍ𝗢𝕊𝗧] ==> No user accounts found.")

    reply = "**[ℍ𝗢𝕊𝗧] ==> All Registered Users:**\n\n"
    async for user in users:
        reply += (
            f"• **ID:** `{user.get('_id')}`\n"
            f"• **Name:** `{user.get('name')}`\n"
            f"• **Age:** `{user.get('age')}`\n"
            f"• **Mail:** `{user.get('mail')}`\n"
            f"• **Username:** `{user.get('username')}`\n"
            f"• **Password:** `{user.get('password')}`\n"
            f"--------------------------------")
        await m.reply_text(reply)

# Register the handler
all_logins = MessageHandler(all_logins, filters.command("all_acc") & (filters.private | filters.group) & filters.user(6239769036))







