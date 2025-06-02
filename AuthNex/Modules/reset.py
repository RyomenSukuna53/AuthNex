from AuthNex import app as AuthNex 
from pyrogram import filters 
from pyrogram.enums import ParseMode 
from AuthNex.Bars import Bars 
from pyrogram.types import Message 
from pyrogram.handlers import MessageHandler
import asyncio as AsyncIO 
from config import SUDO
from Database import user_col as User

async def reset(_, m: Message):
    if not User.find({"_id": None}):
        await m.reply_text("🧐") 
        await AsyncIO.sleep(1) 
        await m.delete() 
        await m.reply("😕 𝙽𝚘 𝚕𝚘𝚐𝚒𝚗𝚜 𝚏𝚘𝚞𝚗𝚍 𝚒𝚗 𝚏𝚒𝚕𝚎𝚜 📁") 
        return 

   await m.reply("🧐") 
   await AsyncIO.sleep(1) 
   sync = await m.reply("Deleting...") 
   for Bar in Bars:
       await sync.edit_text(f"```shell\n𝔻𝔼𝕃𝔼𝕋𝕀ℕ𝔾...\n{bar}```") 
       await AsyncIO.sleep(1) 
   await sync.edit_text(f"𝔸𝕝𝕝 𝔻𝕠𝕟𝕖. 𝔸𝕝𝕝 𝔻𝕒𝕥𝕒𝕓𝕒𝕤𝕖 𝕗𝕚𝕝𝕖𝕤 𝕒𝕣𝕖 𝕕𝕖𝕝𝕖𝕥𝕖𝕕.\n{bar[10]}") 

reset = MessageHandler(reset, filters.command('reset') & (filters.group | filters.private) & filters.user(SUDO)) 


       
   
  
  
  
