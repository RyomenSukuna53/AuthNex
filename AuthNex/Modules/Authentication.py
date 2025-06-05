from pyrogram import Client
import random
from AuthNex.Modules import HelperBot

otp_storage = {}

async def authentication_code(mail: str, target_id: int):
    code = random.randint(10000, 99999)
    otp_storage[target_id] = {"mail": mail, "code": str(code)}

    await HelperBot.send_message(
        chat_id=target_id,
        text=f"🔐 Your authentication code for `{mail}` is: **{code}**"
    )
    return str(code)
