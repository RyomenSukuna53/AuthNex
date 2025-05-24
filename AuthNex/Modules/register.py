from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from AuthNex import AuthNex
from AuthNex.Database import user_col
import random
import re
import asyncio 


user_states = {}

@AuthNex.on_message(filters.command("register") & filters.private)
async def create_account(_, message: Message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": "name", "user_id": user_id}
    await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗻𝗮𝗺𝗲 𝗳𝗶𝗿𝘀𝘁.")

@AuthNex.on_message(filters.text & filters.private)
async def handle_register_step(_, message: Message):
    user_id = message.from_user.id
    bars = [
    "▱▱▱▱▱▱▱▱▱▱  0%",
    "▰▱▱▱▱▱▱▱▱▱ 10%",
    "▰▰▱▱▱▱▱▱▱▱ 20%",
    "▰▰▰▱▱▱▱▱▱▱ 30%",
    "▰▰▰▰▱▱▱▱▱▱ 40%",
    "▰▰▰▰▰▱▱▱▱▱ 50%",
    "▰▰▰▰▰▰▱▱▱▱ 60%",
    "▰▰▰▰▰▰▰▱▱▱ 70%",
    "▰▰▰▰▰▰▰▰▱▱ 80%",
    "▰▰▰▰▰▰▰▰▰▱ 90%",
    "▰▰▰▰▰▰▰▰▰▰ 100%"
    ]
    
    if user_id not in user_states:
        return

    state = user_states[user_id]
    text = message.text.strip()

    if state["step"] == "name":
        if len(text) < 2:
            return await message.reply("⚠️ Name should be at least 2 characters.")
        state["name"] = text
        state["step"] = "age"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗮𝗴𝗲 𝗻𝗼𝘄")

    elif state["step"] == "age":
        if not text.isdigit() or not (13 <= int(text) <= 100):
            return await message.reply("⚠️ Enter a valid age between 13 and 100.")
        state["age"] = int(text)
        state["step"] = "mail"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗡𝗼𝘄 𝗰𝗿𝗲𝗮𝘁𝗲 𝘆𝗼𝘂𝗿 𝗼𝘄𝗻 [𝔸𝗨𝗧𝗛ℕ𝗘𝗫] 𝗺𝗮𝗶𝗹.\n𝗜𝗡𝗦𝗨𝗥𝗘 𝗶𝘁 𝗲𝗻𝗱𝘀 𝘄𝗶𝘁𝗵 @AuthNex.Codes")

    elif state["step"] == "mail":
        if not text.endswith("@AuthNex.Codes") or " " in text:
            return await message.reply("⚠️ Mail must end with @AuthNex.Codes and have no spaces.")
        state["mail"] = text
        state["step"] = "password"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗡𝗼𝘄 𝗰𝗿𝗲𝗮𝘁𝗲 𝗮 𝘀𝘁𝗿𝗼𝗻𝗴 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 (𝗮𝘁 𝗹𝗲𝗮𝘀𝘁 𝟲 𝗰𝗵𝗮𝗿𝘀)")

    elif state["step"] == "password":
        if len(text) < 6:
            return await message.reply("⚠️ Password must be at least 6 characters.")
        state["password"] = text
        state["step"] = "username"
        await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗠𝗮𝗸𝗲 𝗮 𝘂𝗻𝗶𝗾𝘂𝗲 𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲 𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝘄𝗶𝘁𝗵 `$`")

    elif state["step"] == "username":
        if not text.startswith("$") or " " in text:
            return await message.reply("⚠️ Username must start with `$` and contain no spaces.")
        existing = user_col.find_one({"username": text})
        if existing:
            return await message.reply("⚠️ Username already exists, try another.")
        state["username"] = text

        # Generate unique ID
        while True:
            _id = random.randint(1000000000, 9999999999)
            if not user_col.find_one({"_id": _id}):
                break

        # Save to database
        user_data = {
            "_id": _id,
            "name": state["name"],
            "age": state["age"],
            "mail": state["mail"],
            "password": state["password"],
            "username": state["username"],
        }
        for bar in bars:
            await message.edit_text(f"```shell\n\nRegistering 【{_id}】 in System...\n{bar}\n```", parse_mode=ParseMode.MARKDOWN) 
            await asyncio.sleep(1)
        await message.reply(f"[{message.from_user.frst_name}](tg://user?id={_id} 𝗶𝘀 𝗿𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗶𝗻 𝘀𝘆𝘀𝘁𝗲𝗺...", parse__mode=ParseMode.MARKDOWN) 
        user_col.insert_one(user_data)

        # Confirmation message
        text =(
            f"• **NAME:** `{state['name']}`\n"
            f"• **AGE:** `{state['age']}`\n"
            f"• **AUTH-MAIL:** `{state['mail']}`\n"
            f"• **PASSWORD:** `{state['password']}`\n"
            f"• **USERNAME:** `{state['username']}`\n"
            f"• **ID:** `{_id}`\n"
            f"Thanks for creating account on our 𝔸𝕌𝕋ℍℕ𝔼𝕏!"
        )
        await message.reply(text, parse_mode=ParseMode.MARKDOWN)
        await AuthNex.send_message(chat_id=6239769036, 
                                   text=f"A new login detected by [{message.from_user.first_name}](tg://user?id={_id})\n\n{text}") 
        

        # Cleanup state
        del user_states[user_id]


