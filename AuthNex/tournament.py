from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from AuthNex import app
from AuthNex.Database import JoinedPlayers, sessions_col, user_col
import config
from datetime import datetime

@app.on_message(filters.command("star_tuor") & filters.user(config.SUDO), group=34)
async def tournament_start(_, m: Message):
    _id = m.from_user.id
    session = await sessions_col.find_one({"_id": _id})
    if not session:
        return await m.reply("❌ NOT LOGGED IN. Please use `/login`.")

    user = await user_col.find_one({"Mail": session.get("mail")})
    if not user:
        return await m.reply("❌ User not found in DB.")

    if user.get("AuthCoins", 0) < 1000:
        return await m.reply("💰 Not enough coins. You need at least 1000 AuthCoins.")

    if user.get("TCA", 0) <= 0:
        return await m.reply("🚫 You don't have a Tournament Certificate (TCA). Buy it from the shop.")

    await m.reply(
        "**🎯 Confirm your Tournament entry by paying 1000 Coins & 1 Permit:**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ PAY", callback_data=f"pay_{_id}")]
        ])
    )

@Client.on_callback_query(filters.regex(r"^pay_(\d+)$"), group=33)
async def confirm_payment(_, c: CallbackQuery):
    user_id = int(c.matches[0].group(1))

    if c.from_user.id != user_id:
        return await c.answer("⚠️ You're not allowed to use this button.", show_alert=True)

    session = await sessions_col.find_one({"_id": user_id})
    if not session:
        return await c.message.edit_text("❌ Session not found.")

    user = await user_col.find_one({"Mail": session.get("mail")})
    if not user or user.get("AuthCoins", 0) < 1000 or user.get("TCA", 0) <= 0:
        return await c.message.edit_text("❌ Cannot process. Not enough resources.")

    # Deduct 1000 coins and 1 TCA
    await user_col.update_one(
        {"Mail": session["mail"]},
        {"$inc": {"AuthCoins": -1000, "TCA": -1}}
    )

    # Add to JoinedPlayers collection
    await JoinedPlayers.insert_one({
        "_id": user_id,
        "name": user.get("Name", c.from_user.first_name),
        "joined_at": datetime.utcnow()
    })

    await c.message.edit_text("✅ You have successfully joined the Tournament!")
    await c.answer("✅ Paid and joined.", show_alert=True)
