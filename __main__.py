from AuthNex import app as AuthNex
from pyrogram import Client 

from AuthNex.Modules.start import start 
AuthNex.add_handler(start) 

from AuthNex.Modules.register import acc_start 
AuthNex.add_handler(acc_start) 

from AuthNex.Modules.register import acc_steps
AuthNex.add_handler(acc_steps) 

from AuthNex.Modules.delete import del_acc 
AuthNex.add_handler(del_acc) 

from AuthNex.Modules.all_logins import all_logins 
AuthNex.add_handler(all_logins) 

if __name__=="__main__":
  AuthNex.run() 
  print("𝔸𝗨𝗧𝗛ℕ𝗘𝕏 is now started ✅") 
