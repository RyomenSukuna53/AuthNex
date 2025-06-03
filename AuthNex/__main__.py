from AuthNex import app
from AuthNex.Modules import start, reset, register, accounts, login, logout, profile
from AuthNex.Database import *

if __name__=="__main__":
    app.run() 
