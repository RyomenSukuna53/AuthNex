from pyrogram import filters
from AuthNex import app
from AuthNex.Database import user_col  # ensure you import your DB collection

@app.on_message(filters.command("del_account") & filters.private)
async def delete_account(_, message):
    user_id = message.from_user.id
    user_data = user_col.find_one({"user_id": user_id})
    
    if not user_data:
        return await message.reply_text("[ℍ𝗢𝕊𝗧] ==> 𝗡𝗼 𝗮𝗰𝗰𝗼𝘂𝗻𝘁 𝗳𝗼𝘂𝗻𝗱 𝗳𝗼𝗿 𝗱𝗲𝗹𝗲𝘁𝗶𝗼𝗻.")

    confirmation_msg = await message.reply_text(
        "[ℍ𝗢𝕊𝗧] ==> 𝗧𝘆𝗽𝗲: `Sudo delete my account plz` 𝘁𝗼 𝗰𝗼𝗻𝗳𝗶𝗿𝗺 𝗮𝗰𝗰𝗼𝘂𝗻𝘁 𝗱𝗲𝗹𝗲𝘁𝗶𝗼𝗻."
    )

    # Wait for next message from same user
    def check(msg):
        return msg.from_user.id == user_id and msg.text.lower().strip() == "sudo delete my account plz"

    try:
        confirmation = await AuthNex.listen(filters=filters.private & filters.user(user_id), timeout=60)
    except TimeoutError:
        return await message.reply_text("[ℍ𝗢𝕊𝗧] ==> 𝗧𝗶𝗺𝗲𝗼𝘂𝘁. 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗻𝗼𝘁 𝗱𝗲𝗹𝗲𝘁𝗲𝗱.")

    await user_col.delete_one({"user_id": user_id})

    await message.reply_text("[ℍ𝗢𝕊𝗧] ==> ✅ 𝗬𝗼𝘂𝗿 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗲𝗹𝗲𝘁𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆.")

    # Logging to admin
    await app.send_message(
        chat_id=6239769036,
        text=(
            f"[ℍ𝗢𝕊𝗧] ==> One account deleted by [{message.from_user.first_name}](tg://user?id={user_id})\n\n"
            f"• Name: {user_data.get('name')}\n"
            f"• Age: {user_data.get('age')}\n"
            f"• Mail: {user_data.get('mail')}\n"
            f"• Username: {user_data.get('username')}\n"
            f"• ID: {user_data.get('_id')}"
        ),
        parse_mode="markdown"
    )

