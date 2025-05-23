from setuptools import setup, find_packages

setup(
    name="AuthNex",
    version="1.0.0",
    description="Telegram-based Auth System by AuthNex",
    author="𝙆𝙐𝙍𝙊-𝙍𝘼𝙄𝙅𝙄𝙉",
    author_email="sufyan532011@gmail.com",
    url="https://github.com/RyomenSukuna53/AuthNex",
    packages=find_packages(),
    install_requires=[
        "pyrogram",
        "tgcrypto",
        "motor"
    ],
    python_requires=">=3.10"
)

