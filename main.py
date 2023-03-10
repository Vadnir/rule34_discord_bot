from Rule import Rule
from dotenv import load_dotenv
from discord.ext import commands
import os
import discord

load_dotenv()
token = os.getenv("discord_token")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
rule = Rule()


@bot.event
async def on_ready():
    print("Bot Iniciado")


@bot.command()
@commands.is_nsfw()
async def random_posta(ctx, *args):
    for _ in range(5):
        post = await rule.random_post(tags=list(args))
        if post is None:
            await ctx.send("No Imagen Related Found")
            return
        await ctx.send(post)


@bot.command()
@commands.is_nsfw()
async def search(ctx, limit: int = 10, page: int = 10, *tags):
    posts = await rule.search(tags=list(tags), limit=limit, page=page)
    if posts is None:
        await ctx.send("No Imagen Related Found")
        return

    [await ctx.send(i) for i in posts]


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.NSFWChannelRequired):
        await ctx.send("NSFW Command")

bot.run(token)
