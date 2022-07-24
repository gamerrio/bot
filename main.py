import discord
from discord.ext import commands
import json
import random

bot = commands.Bot(command_prefix=commands.when_mentioned_or("*")) # prefix for calling the bot (or when mentioned)

f = open('config.json', "r")
token = json.loads(f.read()) # config.json has the token as a string


@bot.event
async def on_ready():
    print(f"{bot.user} is ready!") #executed when bot is deployed and ready


@bot.command(description="returns the latency", brief="*ping")
async def ping(ctx):
    await ctx.send(f"✅ The ping is: {round(bot.latency, 4)} seconds.")


@bot.command(description="returns a random number between two args if given", brief="*rng [from this] [to this]")
async def rng(ctx, first='1', last='100'):
    if first >= last:
        await ctx.send("The second value has to be greater than the first value.")
    else:
        await ctx.send(random.randint(int(first), int(last)))





bot.run(token)
