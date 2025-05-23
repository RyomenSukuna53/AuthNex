from AuthNex import AuthNex 
from pyrogram import Client, filters 

@AuthNex.on_message(filters.command("del_account"))
async def delete_account(_, message):
  _id =  user_col.find_one({"_id": _id}) 
  if not _id:
    return 
  else:
    text = "𝚂𝚞𝚍𝚘 𝚍𝚎𝚕𝚎𝚝𝚎 𝚖𝚢 𝚊𝚌𝚌𝚘𝚞𝚗𝚝 𝚙𝚕𝚣"
    msg = await message.reply_text(f"[ℍ𝗢𝕊𝗧] ==> 𝗧𝘆𝗽𝗲: `𝚂𝚞𝚍𝚘 𝚍𝚎𝚕𝚎𝚝𝚎 𝚖𝚢 𝚊𝚌𝚌𝚘𝚞𝚗𝚝 𝚙𝚕𝚣`")
    if text in message.text:
      await message.reply_text("[ℍ𝗢𝕊𝗧] ==> ID DELETED SUCCESSFULLY \nThanks for using our  𝔸𝗨𝗧𝗛ℕ𝗘𝕏.")
      info = user_col.find_one({
            "_id": _id,
            "name": None,
            "age": None,
            "mail": None,
            "password": None, 
            "username": None
        }) 
      await AuthNex.send_message(chat_id=6239769036, text=f"[ℍ𝗢𝕊𝗧] ==> One id deleted by [{message.from_user.first_name}](tg://user?id={_id})\n
      {info}") 
      await user_col.delete_one({"_id": _id}) 
    else:
      return await msg.reply("[ℍ𝗢𝕊𝗧] ==> Wrong way. Use the replied one") 
    
