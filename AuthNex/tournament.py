from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ParseMode
from AuthNex import app
from AuthNex.Datbase import players
import config
@Client.on_message(filter.command("startuor") & filters.user(config.SUDO))
async def TUORNAMENT(_, m: Message):
    pass
