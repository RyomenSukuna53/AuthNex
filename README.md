Certainly! Here's a comprehensive README.md for your AuthNex Telegram bot project, tailored to its current structure and features:


---

AuthNex

AuthNex is a robust Telegram bot designed for secure user authentication and session management. Built using Pyrogram and MongoDB, it offers functionalities like OTP-based login, user data retrieval, and session tracking.

🚀 Features

Secure Login: Authenticate users via email and password, followed by OTP verification.

OTP Generation: Send one-time passwords to users for enhanced security.

Session Management: Track user sessions with login timestamps.

User Information Retrieval: Fetch and display user details from the database.

Modular Codebase: Organized structure for scalability and maintainability.


📁 Project Structure

AuthNex/
├── AuthNex/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── Database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── models.py
│   └── Modules/
│       ├── __init__.py
│       ├── Authentication.py
│       ├── login.py
│       └── verify.py
├── requirements.txt
├── setup.py
└── README.md

🛠️ Installation

Prerequisites

Python 3.10 or higher

MongoDB instance (local or cloud-based)

Telegram API credentials


Steps

1. Clone the Repository

git clone https://github.com/RyomenSukuna53/AuthNex.git
cd AuthNex


2. Install Dependencies

pip install -r requirements.txt


3. Configure Environment Variables

Create a .env file in the root directory and add the following:

API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_bot_token
MONGO_URI=your_mongodb_connection_string


4. Run the Bot

python -m AuthNex



🔐 Usage

/login

Initiates the login process.

1. User sends /login command.


2. Bot prompts for email.


3. User provides email.


4. Bot prompts for password.


5. User provides password.


6. Bot verifies credentials and sends an OTP to the user's Telegram account.


7. User enters the OTP.


8. Bot verifies the OTP and completes the login process.



/info

Retrieves user information.

/info user@example.com

Displays details like name, age, AuthCoins balance, and last login time.

🧩 Modules Overview

Authentication.py

authentication_code(mail, target_id): Generates and sends an OTP to the specified Telegram user ID.

otp_storage: Dictionary to temporarily store OTPs for verification.


login.py

Handles the /login command.

Manages the multi-step login process: email → password → OTP.


verify.py

Handles OTP verification.

Confirms user identity and finalizes the login process.


🧪 Testing

To test the bot:

1. Start the bot using python -m AuthNex.


2. Open Telegram and search for your bot.


3. Initiate the login process with /login.


4. Follow the prompts to complete authentication.



📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.


---

Feel free to customize this README.md further to match any additional features or changes in your project.

