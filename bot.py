import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} est connecté !')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!stats'):
        await message.channel.send("Tu veux de l'aide avec la moyenne, l’écart-type, l’ANOVA ?")

client.run(TOKEN)
