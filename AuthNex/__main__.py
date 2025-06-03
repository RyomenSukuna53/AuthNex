from AuthNex import app
from pyrogram import Client
from AuthNex.Modules.start import start
from AuthNex.Modules.register import acc_start
from AuthNex.Modules.reset import ResetHandlerObject
from AuthNex.Modules.register import acc_steps
from AuthNex.Modules.accounts import accounts_handler_obj
from AuthNex.Modules.logs import logs
from AuthNex.Modules.LoginAndLogout import login1
from AuthNex.Modules.LoginAndLogout import login2
from AuthNex.Modules.LoginAndLogout import logout
from AuthNex.Modules.LoginAndLogout import profile


app.add_handler(start)
app.add_handler(acc_start)
app.add_handler(acc_steps)
app.add_handler(ResetHandlerObject)
app.add_handler(accounts_handler_obj)
app.add_handler(logs) 
app.add_handler(login1)
app.add_handler(login2)
app.add_handler(logout)
app.add_handler(profile)


if __name__=="__main__":
  app.run()
  print("𝔸𝗨𝗧𝗛ℕ𝗘𝕏 is now started ✅")
