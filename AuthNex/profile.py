from AuthNex import app
from AuthNex.Database import user_col, sessions_col
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

@Client.on_message(filters.command('info'), group=6)
async def info(_, m: Message):
    user = m.from_user
    _id = user.id

    # Ensure the command has an argument (e.g. /info email)
    if len(m.command) != 2:
        return await m.reply_text("**𝗜𝗻𝘃𝗮𝗹𝗶𝗱 ❌**\n𝗨𝗦𝗔𝗚𝗘: `/info yourmail@AuthNex.Codes`", parse_mode=ParseMode.MARKDOWN)

    mail = m.command[1]

    if not mail.endswith("@AuthNex.Codes"):
        return await m.reply("**Invalid ❌**\n𝗨𝗦𝗔𝗚𝗘: `/info mail@AuthNex.Codes`", parse_mode=ParseMode.MARKDOWN)

    user_data = await user_col.find_one({"Mail": mail})
    session_data = await sessions_col.find_one({"mail": mail})
    my_session = await sessions_col.find_one({"_id": _id})

    if not user_data:
        return await m.reply("**❌ Invalid Mail**")

    msg = f"""
╭─❖〔 👤 𝗨𝗦𝗘𝗥 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 〕❖─╮
│ 🆔 𝗜𝗗: {session_data.get('_id')}
│ 👤 𝗡𝗮𝗺𝗲: {user.get('Name')}
│ 📧 𝗘𝗺𝗮𝗶𝗹: {user.get('Mail')}
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
    await m.reply_text(msg)
