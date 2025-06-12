from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
from AuthNex import app
from AuthNex.Database import user_col, sessions_col

@Client.on_message(filters.command('myinfo') & (filters.private), group=16)
async def accounts_handler(client: Client, m: Message):
    _id = m.from_user.id

    # Check if session exists
    session = await sessions_col.find_one({"_id": _id})
    if not session:
        return await m.reply("❌ You are not logged in. Use `/login` first.")

    # Fetch user data
    user = await user_col.find_one({"Mail": session.get('mail')})
    if not user:
        return await m.reply("❌ User data not found.")

    # Fetch profile picture
    photos = await client.get_profile_photos(_id, limit=1)
    if not photos:
        return await m.reply("❌ No profile picture found.")

    # Download profile pic
    pic = await client.download_media(photos[0].file_id)
    msg = f"""
    ╭─❖〔 👤 𝗨𝗦𝗘𝗥 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 〕❖─╮
    │ 🆔 𝗜𝗗: {user.get('_id')}
    │ 👤 𝗡𝗮𝗺𝗲: {user.get('Name')}
    │ 📧 𝗘𝗺𝗮𝗶𝗹: {user.get('Mail')}
    │ 🧪 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱: `{user.get('Password')}`
    | 🔑 𝗧𝗼𝗸𝗲𝗻: `{user.get('token', 'Not Generated')}`
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
    # Reply with info and profile pic
    await m.reply_photo(
        photo=pic,
        caption=msg,
        parse_mode=ParseMode.MARKDOWN
    )



