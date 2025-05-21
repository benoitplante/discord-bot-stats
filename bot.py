import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True  # Assure-toi que les messages sont gérés
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} est connecté !')

@client.event
async def on_message(message):
    print(f"Message reçu : {message.content}")  # Pour debug dans les logs

    if message.author == client.user:
        return

    if message.content.lower().startswith('!stats'):
        await message.channel.send("Statistiques ? Je suis là pour t'aider !")

client.run(TOKEN)

