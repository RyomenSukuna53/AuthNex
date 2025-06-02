from AuthNex import app as AuthNex
from pyrogram import Client
from AuthNex.Modules.start import start
from AuthNex.Modules.register import acc_start
from AuthNex.Modules.reset import ResetHandlerObject
from AuthNex.Modules.register import acc_steps
from AuthNex.Modules.accounts import accounts_handler_obj
from AuthNex.Modules.logs import logs

AuthNex.add_handler(start)
AuthNex.add_handler(acc_start)
AuthNex.add_handler(acc_steps)
AuthNex.add_handler(ResetHandlerObject)
AuthNex.add_handler(accounts_handler_obj)
AuthNex.add_handler(logs) 


if __name__=="__main__":
  AuthNex.run() 
  print("𝔸𝗨𝗧𝗛ℕ𝗘𝕏 is now started ✅") 
