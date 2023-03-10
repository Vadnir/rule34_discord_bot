from Rule import Rule
from dotenv import load_dotenv
import os
import discord

load_dotenv()
token = os.getenv("discord_token")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
rule = Rule()


@client.event
async def on_ready():
    print("Bot Iniciado")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if not message.content.startswith('$random_post'):
        return

    if not message.channel.nsfw:
        await message.channel.send("El Canal no es nfsw")
        return

    temp = message.content.replace("$random_post", "").split(" ")
    tags = []

    for i in temp:
        if i != "":
            tags.append(i)

    for i in range(5):
        await message.channel.send(await rule.random_post(tags=tags))

client.run(token)
