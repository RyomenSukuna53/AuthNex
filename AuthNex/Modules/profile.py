from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatType
from AuthNex import bot
from AuthNex.Database import user_col, session_col


@Client.on_message(filters.command('info'))
async def info(_, m: Message):
    user = message.from_user
    _id = user.id
    if len(message.text) != 2:
        return await m.reply_text("**𝗜𝗻𝘃𝗮𝗹𝗶𝗱 ❌**\n𝗨𝗦𝗔𝗚𝗘: /info <mail>")
    text = message.text[1]
    if not text.endswith("@AuthNex.Codes"):
        return await m.reply("**Invalid ❌**\n𝗨𝗦𝗔𝗚𝗘: /info <mail>[Ensure that mail ends with @AuthNex.Codes")
    mail = message.text[1]
    user = await user_col.find_one({"Mail": mail})
    session = await sessions_col.find_one({"mail": mail})
    if not user:
        return await m.reply("**Invalid Mail**")
    MySession = sessions_col.find_one({"_id": _id}) 
    reply = f"𝙸𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝙼𝚊𝚒𝚕[{mail}]\n\n"
    if not MySession:
        reply += f"**NAME:** `{user['Name']}|\n"
        reply += f"**AGE:** `{user['Age']}`\n"
        reply += f"**AUTH-COINS:** `{user['AuthCoins']}`\n"
        reply += f"**LOGINED-BY:** `[{session['name']}](tg://user?id={session['_id']})\n"
        reply += f"**LAST LOGIN:** {session['login']}"
        await m.reply(reply)
        return 
    if MySession:
        reply += f"**NAME:** `{user['Name']}|\n"
        reply += f"**AGE:** `{user['Age']}`\n"
        reply += f"**AUTH-COINS:** `{user['AuthCoins']}`\n"
        reply += f"**OWNER:** `[{user['Onwer']}](tg://user?id={session['_id']})\n"
        reply += f"**LAST LOGIN:** {session['login']}"
        await m.reply(reply)
    
