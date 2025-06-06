# AuthNex/AuthClient.py

from AuthNex.Database import user_col, sessions_col, tokens_col
from pyrogram import Client

class AuthNexClient:
    def __init__(self, email, password, name, token, coins=50):
        self.email = email
        self.password = password
        self.name = name
        self.token = token
        self.coins = coins
        self.verified_user = None

    async def connect(self):
        # Check if user exists
        user = await user_col.find_one({"Mail": self.email})
        token = await tokens_col.find_one({"token": token})
        if not user:
            raise ValueError("❌ Email not registered.")

        if not token:
             raise ValueError("🚫 Token is not registered")
        # Check token, name, and password
        if (
            user.get("Password") != self.password or
            user.get("Name") != self.name
        ):
            raise ValueError("❌ Credentials mismatch or invalid token.")

        self.verified_user = user
        self.coins = user.get("coins", self.coins)
        return f"✅ Connected to AuthNex as {self.name} with {self.coins} AuthCoins"
      
