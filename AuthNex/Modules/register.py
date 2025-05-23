from pyrogram import Client, filters 
from pyrogram.enums import ChatType, ParseMode 
from pyrogram.types import InlineKeyboardButton, İnlineKeyboardMakrup, CallbackQuery 
from AuthNex import AuthNex 
from AuthNex.Database import *
import random 

user_states = {}

@bot.on_message(filters.command("register") & filters.private)
async def create_account(_, message: Message):
    user_id = message.from_user.id
    

    user_states[user_id] = {"step": "name", "user_id": user_id}
    await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗻𝗮𝗺𝗲 𝗳𝗶𝗿𝘀𝘁.")

@bot.on_message(filters.text & filters.private & ~filters.command(["order"], prefixes=HANDLERS))
async def handle_order_step(_, message: Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        return

    state = user_states[user_id]

    if state["step"] == "name":
        state["name"] = message.text
        state["step"] = "age"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗮𝗴𝗲 𝗻𝗼𝘄")

    elif state["step"] == "age":
        state["age"] = int(message.text) 
        state["step"] = "mail"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗻𝗼𝘄 𝗰𝗿𝗲𝗮𝘁𝗲 𝘆𝗼𝘂𝗿 𝗼𝘄𝗻 [𝔸𝗨𝗧𝗛ℕ𝗘𝗫] 𝗺𝗮𝗶𝗹.\n𝗜𝗡𝗦𝗨𝗥𝗘 𝘁𝗵𝗮𝘁 𝘆𝗼𝘂𝗿 𝗺𝗮𝗶𝗹 𝗲𝗻𝗱𝘀 𝗼𝗻 @AuthNex.Codes")

    elif state["step"] == "mail":
        state["mail"] = message.text
        state["step"] = "password"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗡𝗼𝘄 𝗰𝗿𝗲𝗮𝘁𝗲 𝗮 𝘀𝘁𝗿𝗼𝗻𝗴 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱") 
    elif state["step"] == "password":
        state["password"] = message.text
        state["step"] = "username"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗠𝗮𝗸𝗲 𝗮 𝘀𝗽𝗲𝗰𝗶𝗳𝗶𝗰 𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲.\n𝗘𝗻𝘀𝘂𝗿𝗲 𝘁𝗵𝗮𝘁 𝘆𝗼𝘂𝗿 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 𝘀𝘁𝗮𝗿𝘁 𝘄𝗶𝘁𝗵 $.")

    elif state["step"] == "username":
     state["username"] == message.text

    _id = random.randint(1000000000, 10000000000) 
    ud = user_col.find_one("_id": _id) 
    if ud:
      _id = random.randint(1000000000, 10000000000) 
      
    text = (
            f"✅ **Confirm Your Order**\n\n"
            f"• **NAME:** `{state['name']}`\n"
            f"• **AGE:** `{state['age']}`\n"
            f"• **AUTH-MAIL:** `{state['mail']}`\n"
            f"• **PASSWORD:** `{state['password']}`\n"
            f"• **USERNAME:** {state['username']}\n"
            f"• **ID:** `{_id}\n"
            f"Thanks for creating account on our 𝔸𝕌𝕋ℍℕ𝔼𝕏"
        )
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

    user_col.insert_one

    

            
            del user_states[user_id]

        


  
