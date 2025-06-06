from pyrogram import Client, filters
from pyrogram.types import Message
from AuthNex import app
from AuthNex.Database import user_col
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

@Client.on_message(filters.command("myinfo") & filters.private, group=13)
async def my_info(client, message: Message):
    user = message.from_user
    user_id = user.id

    # Get user data from MongoDB
    user_data = await user_col.find_one({"_id": user_id})
    if not user_data:
        return await message.reply("❌ No account found. Please create one.")

    token = user_data.get("token", "Not generated")
    email = user_data.get("Mail", "Not set")

    # Get profile pic
    photos = await client.get_profile_photos(user.id, limit=1)
    if not photos:
        return await message.reply("❌ No profile picture found. Please set one on Telegram.")

    photo = photos[0]
    file = await client.download_media(photo.file_id)
    pfp = Image.open(file).convert("RGBA").resize((512, 512))

    # Create canvas
    base = Image.new("RGBA", (700, 800), (0, 0, 0, 255))
    base.paste(pfp, (94, 70))  # center the profile pic

    draw = ImageDraw.Draw(base)

    # Load custom fonts (optional)
    try:
        font_big = ImageFont.truetype("arial.ttf", 50)
        font_small = ImageFont.truetype("arial.ttf", 30)
    except:
        font_big = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Draw text
    draw.text((180, 10), "AUTHNEX PROFILE", font=font_big, fill=(0, 255, 255, 255))
    draw.text((100, 600), f"👤 Username: {user.first_name}", font=font_small, fill="white")
    draw.text((100, 640), f"📧 Email: {email}", font=font_small, fill="white")
    draw.text((100, 680), f"🔑 Token: {token[:12]}...", font=font_small, fill="white")
    draw.text((100, 720), f"🆔 ID: {user.id}", font=font_small, fill="white")

    # Save final image
    output = BytesIO()
    output.name = "authnex_profile.png"
    base.save(output, format="PNG")
    output.seek(0)

    # Send image + text
    await message.reply_photo(
        photo=output,
        caption=f"""**👤 AuthNex Profile**
🆔 ID: `{user.id}`
📧 Email: `{email}`
🔑 Token: `{token}`""",
        parse_mode="markdown"
    )
