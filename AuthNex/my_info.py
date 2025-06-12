from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from AuthNex import app
from AuthNex.Database import user_col, sessions_col

@Client.on_message(filters.command('myinfo') & filters.private, group=16)
async def accounts_handler(client: Client, m: Message):
    _id = m.from_user.id

    session = await sessions_col.find_one({"_id": _id})
    if not session:
        return await m.reply("❌ You are not logged in. Use `/login` first.")

    user = await user_col.find_one({"Mail": session.get('mail')})
    if not user:
        return await m.reply("❌ User data not found.")

    # Get chat info (including photo)
    chat = await client.get_chat(_id)
    pic = None
    if chat.photo:
        pic = await client.download_media(chat.photo.big_file_id)

    msg = f"""
╭─❖〔 👤 𝗨𝗦𝗘𝗥 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 〕❖─╮
│ 🆔 𝗜𝗗: `{_id}`
│ 👤 𝗡𝗮𝗺𝗲: {user.get('Name')}
│ 📧 𝗘𝗺𝗮𝗶𝗹: {user.get('Mail')}
│ 🧪 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱: `{user.get('Password')}`
│ 🔑 𝗧𝗼𝗸𝗲𝗻: `{user.get('token', 'Not Generated')}`
├──────── 💰 𝗖𝗨𝗥𝗥𝗘𝗡𝗖𝗜𝗘𝗦 ────────┤
│ 💶 𝗘𝘂𝗿𝗼: {user.get('euro', 0)}
│ 💵 𝗗𝗼𝗹𝗹𝗮𝗿: {user.get('dollar', 0)}
│ 💴 𝗬𝗲𝗻: {user.get('yen', 0)}
│ 🪙 𝗕𝗶𝘁𝗰𝗼𝗶𝗻: {user.get('bitcoin', 0)}
│ 🌀 𝗔𝘂𝘁𝗵𝗖𝗼𝗶𝗻𝘀: {user.get('AuthCoins', 0)}
├─────── 🏆 𝗧𝗢𝗨𝗥𝗡𝗔𝗠𝗘𝗡𝗧 ───────┤
│ 🎟️ 𝗣𝗲𝗿𝗺𝗶𝘁𝘀: {user.get('tca', 0)}
╰─────────────────────────────╯
"""

    if pic:
        await m.reply_photo(pic, caption=msg, parse_mode=ParseMode.MARKDOWN)
    else:
        await m.reply(msg, parse_mode=ParseMode.MARKDOWN)
