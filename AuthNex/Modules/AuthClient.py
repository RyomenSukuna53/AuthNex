from pyrogram import Client
from AuthNex.Database import user_col
import os

class AuthClient(Client):
    def __init__(
        self,
        api_id: int,
        api_hash: str,
        bot_token: str,
        coins: int,
        mail: str,
        password: str,
        name: str,
        token: str,
        session_name: str = "AuthNexBot"
    ):
        # Inherit Pyrogram Client
        super().__init__(session_name, api_id=api_id, api_hash=api_hash, bot_token=bot_token)

        # AuthNex Details
        self.mail = mail
        self.password = password
        self.name = name
        self.token = token
        self.coins = coins
        self.auth_user = None
        self.auth_connected = False

    async def start(self):
        await super().start()  # Start Pyrogram Bot Client

        user = await user_col.find_one({"Mail": self.mail})
        if not user:
            raise ValueError("❌ Email not registered in AuthNex.")

        if (
            user.get("Password") != self.password or
            user.get("Name") != self.name or
            user.get("token") != self.token
        ):
            raise ValueError("❌ Invalid AuthNex credentials or token mismatch.")

        self.auth_user = user
        self.coins = user.get("coins", self.coins)
        self.auth_connected = True
        print(f"✅ Pyrogram + AuthNex connected as {self.name} with {self.coins} AuthCoins.")

    async def stop(self, *args):
        await super().stop()
        self.auth_user = None
        self.auth_connected = False
        print("❌ Disconnected from AuthNex and Bot.")
