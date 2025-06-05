from pyrogram import Client
from config import *

app = Client("AuthNexLogins",
                 api_id=API_ID,
                 api_hash=API_HASH,
                 bot_token=BOT_TOKEN,
                 plugins=dict(root="AuthNex")
                )

import logging

logging.basicConfig(
  format="[KuroAI-Beta] %(name)s - %(levelname)s - %(message)s",
  handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
  level=logging.INFO,
)

logger = logging.getLogger(__name__)

HelperBot = Client("HelperBot",
                   api_id=27548865,
                   api_hash="db07e06a5eb288c706d4df697b71ab61",
                   bot_token="7883663341:AAEXp8lzLUlY5JVmF770v8bnmp8lsklXhgQ")
