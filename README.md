إليك محتوى ملف README.md باللغة الإنجليزية مع إضافة الحقوق لخالد ولحسن البوت:

# Hassan Discord Bot

## Description
A Discord bot that allows you to manage your server via command line. It provides features like deleting channels, creating channels, banning members, and more. The bot will ask for the token and display the servers it’s part of. Then, you can select the server by its ID.

## Requirements

1. Python 3.8 or higher
2. `discord.py` library

## Installation & Setup

### Step 1: Install Python
If you’re using Termux, you can install Python with:

```bash
pkg install python

Step 2: Install Dependencies

Install the required libraries using:

pip install discord.py

Step 3: Set Up Token

Open bot.py and replace "YOUR_BOT_TOKEN_HERE" with your bot token from the Discord Developer Portal.

Step 4: Run the Bot

Run the bot with the following command:

python bot.py

The bot will ask for the token first, then display the servers it’s connected to. After that, you’ll be prompted to enter the server ID you want to manage.

Step 5: Use Available Commands

Once the server is selected, you can use the menu to execute commands like deleting channels, adding channels, banning users, changing the server name, etc.

Available Commands
	•	1 - Full: Delete channels, create channels, and spam messages.
	•	2 - Delete channels.
	•	3 - Create channels.
	•	4 - Delete roles.
	•	5 - Create roles.
	•	6 - Spam messages via webhooks.
	•	7 - Ban all members.
	•	8 - Change server name.
	•	9 - Change server icon.
	•	10 - Rename all channels.

Notes
	•	Ensure the bot has the necessary permissions to perform the commands.
	•	It might take time for some actions to complete depending on the server’s size.

Credits
	•	Bot developed by Khaled
	•	Bot name and concept by Hassan

License

This project is licensed under the MIT License.

This version is concise, includes the necessary credits, and is written in English. You can now add it to your project’s `README.md`.
