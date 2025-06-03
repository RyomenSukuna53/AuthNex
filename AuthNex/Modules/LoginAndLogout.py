from pyrogram.filters import *
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from AuthNex import app
from AuthNex.Database import user_col

steps = {}

async def login(_, m:Message):
    _id = message.from_user.id
    user = user_col.find_one({"_id": _id,
                              "Login": True})
   
    if user.get("Login") == True:
        await m.reply("💔 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗹𝗼𝗴𝗴𝗲𝗱 𝗶𝗻 𝗮𝘀 {user.get('name')\n𝗟𝗼𝗴𝗼𝘂𝘁 𝗳𝗶𝗿𝘀𝘁 𝘁𝗼 𝗹𝗼𝗴𝗶𝗻 𝗶𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗮𝗰𝗰𝗼𝘂𝗻𝘁.")
        return
    step = steps[_id]
    step["AccountID"] == "
    await m.reply("𝗚𝗶𝘃𝗲 𝗺𝗲 𝘁𝗵𝗲 𝗶𝗱 𝗼𝗳 𝘁𝗵𝗲 𝗮𝗰𝗰𝗼𝘂𝗻𝘁") 
    
    
    
