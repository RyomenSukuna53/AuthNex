from pyrogram.filters import *
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from AuthNex import app
from AuthNex.Database import user_col

user_states = {}

async def login(_, m:Message):
    _id = message.from_user.id
    user = user_col.find_one({"_id": _id,
                              "Login": True})
   
    if user.get("Login") == True:
        await m.reply("💔 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗹𝗼𝗴𝗴𝗲𝗱 𝗶𝗻 𝗮𝘀 {user.get('name')\n𝗟𝗼𝗴𝗼𝘂𝘁 𝗳𝗶𝗿𝘀𝘁 𝘁𝗼 𝗹𝗼𝗴𝗶𝗻 𝗶𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗮𝗰𝗰𝗼𝘂𝗻𝘁.")
        return
    user_states[user_id] = {"step": "name", "user_id": user_id}
    await message.reply("[ℍ𝗢𝕊𝗧] ==> 𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗶𝗱 𝗼𝗳 𝘁𝗵𝗲 𝗮𝗰𝗰𝗼𝘂𝗻𝘁.")

# Step 2–6: Handle Input Steps
async def handle_login_step(_, message: Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        return

    state = user_states[user_id]
    text = message.text.strip()

    
        del user_states[user_id]
        
# Handlers
acc_start = MessageHandler(create_account, filters.command("Create_Acc") & filters.private)
acc_steps = MessageHandler(handle_register_step, filters.private)
    
