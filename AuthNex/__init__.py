from pyrogram import Client
from config import *

app = Client("AuthNexLogins",
                 api_id=API_ID,
                 api_hash=API_HASH,
                 bot_token=BOT_TOKEN,
                 plugins=dict(root="AuthNex")
                )

auth_bot = Client("Helper",
                  api_id=21218274,
                  api_hash="3474a18b61897c672d315fb330edb213",
                  bot_token="7883663341:AAEXp8lzLUlY5JVmF770v8bnmp8lsklXhgQ",
                  plugins=dict(root="AuthNex")
                 )
import logging

logging.basicConfig(
  format="[KuroAI-Beta] %(name)s - %(levelname)s - %(message)s",
  handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
  level=logging.INFO,
)

logger = logging.getLogger(__name__)

