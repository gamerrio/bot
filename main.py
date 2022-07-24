import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="*")

f = open('config.json', "r")
token = json.loads(f.read())


@bot.event
async def on_ready():
    print("Botto is ready!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"✅ The ping is: {round(bot.latency, 4)} seconds.")


bot.run(token)
