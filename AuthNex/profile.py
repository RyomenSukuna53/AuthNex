from AuthNex import app
from AuthNex.Database import user_col, sessions_col
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatType


@Client.on_message(filters.command('info'), group=1)
async def info(_, m: Message):
    user = m.from_user
    _id = user.id
    if len(m.text) != 2:
        return await m.reply_text("**𝗜𝗻𝘃𝗮𝗹𝗶𝗱 ❌**\n𝗨𝗦𝗔𝗚𝗘: /info <mail>")
    text = m.text[1]
    if not text.endswith("@AuthNex.Codes"):
        return await m.reply("**Invalid ❌**\n𝗨𝗦𝗔𝗚𝗘: /info <mail>[Ensure that mail ends with @AuthNex.Codes")
    mail = m.text[1]
    user = await user_col.find_one({"Mail": mail})
    session = await sessions_col.find_one({"mail": mail})
    if not user:
        return await m.reply("**Invalid Mail**")
    MySession = sessions_col.find_one({"_id": _id}) 
    reply = f"𝙸𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝙼𝚊𝚒𝚕[{mail}]\n\n"
    if not MySession:
        reply += f"**NAME:** `{user_col.get('Name')}|\n"
        reply += f"**AGE:** `{user_col.get('Age')}`\n"
        reply += f"**AUTH-COINS:** `{user_col.get('AuthCoins')}`\n"
        reply += f"**LOGINED-BY:** `[{sessions_col.get('name')}](tg://user?id={sessions_col.get('_id')})\n"
        reply += f"**LAST LOGIN:** {sessions_col.get('login')}"
        await m.reply(reply, parse_mode=ParseMode.MARKDOWN)
        return 
    if MySession:
        reply += f"**NAME:** `{user_col.get('Name')}|\n"
        reply += f"**AGE:** `{user_col.get('Age')}`\n"
        reply += f"**AUTH-COINS:** `{user_col.get('AuthCoins')}`\n"
        reply += f"**LOGINED-BY:** `[{sessions_col.get('name')}](tg://user?id={sessions_col.get('_id')})\n"
        reply += f"**LAST LOGIN:** {sessions_col.get('login')}"
        await m.reply(reply, parse_mode=ParseMode.MARKDOWN)
