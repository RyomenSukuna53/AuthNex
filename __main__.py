from AuthNex import app as AuthNex
from pyrogram import Client 
from AuthNex.Modules.start import start 
from AuthNex.Modules.register import acc_start
from AuthNex.Modules.reset import reset_handler 
from AuthNex.Modules.register import acc_steps

AuthNex.add_handler(start) 
AuthNex.add_handler(acc_start) 
AuthNex.add_handler(acc_steps) 
AuthNex.add_handler(reset_handler) 


if __name__=="__main__":
  AuthNex.run() 
  print("𝔸𝗨𝗧𝗛ℕ𝗘𝕏 is now started ✅") 
