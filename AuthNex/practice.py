from pyrogram import import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums ChatType, ParseMode
from AuthNex import app
from AuthNex.Database import sessions_col
@Client.on_message(filters.command("practice"), group=27)
async def PracticeForTournament(_, m: Message):
    _id = m.from_user.id
    if not await sessions_col.find_one({"_id": _id}):
        return
    await m.reply("100 COINS need for training pay first", InlineKeyboardMarkup([
    InlineKeyboardButtton("PAY", callbackdata=f"pay_{_id}")
    ])
@Client.on_mesaage(filters.regex("^pay"), group=28)
async def payout(_, cb: CallbackQuery):
    userID = cb.data.split("_")
    sessons = await sessions_col.find_one({"_id": userID})
    mail = await user_col.find_one({"Mail": sessions.get("mail")})
    if await mail.get("AuthCoins", 0)<50:
        return await m.reply("NOT ENOUGH COINS ", show_alert=True)
    await cb.edit_text("COINS DEDUCTED SUCCESSFULLY...")
    await user_col.update_one({"Mail": mail, {"$inc", {"AuthCoins": -100}
                                             }
                              })
    await m..reply("@gamee Gravity Ninja")
