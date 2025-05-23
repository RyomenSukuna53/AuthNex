from pyrogram import Client 
from config import *

AuthNex = Client("AuthNex",
                 api_id=API_ID, 
                 api_hash=API_HASH, 
                 bot_token=BOT_TOKEN, 
                 plugins=dict(root="(AuthNex/Modules)") 
                ) 

import logging

logging.basicConfig(
    level=logging.INFO,
    format="[KURO-ZONE] %(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)                            
