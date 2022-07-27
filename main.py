import discord
from discord.ext import commands
import json
import random

# prefix for calling the bot (or when mentioned)
bot = commands.Bot(command_prefix=commands.when_mentioned_or("*"))

f = open('config.json', "r")
token = json.loads(f.read())  # config.json has the token as a string


@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")  # executed when bot is deployed and ready


@bot.command(description="returns the latency", brief="*ping")
async def ping(ctx):
    await ctx.send(f"✅ The ping is: {round(bot.latency, 4)} seconds.")
    print(f"{ctx.author} executed ping")


@bot.command(description="returns a random number between two args if given", brief="*rng [from this] [to this]")
async def rng(ctx, first='1', last='100'):
    if first >= last:
        await ctx.send("The second value has to be greater than the first value.")
        print(f"{ctx.author} executed rng (args error)")
    else:
        await ctx.send(random.randint(int(first), int(last)))
        print(f"{ctx.author} executed rng (success)")


@bot.command(description="calculates gpa with A and B grades as inputs", brief="*gpa [a grades] [b grades]")
async def gpa(ctx, *args):
    if len(args) != 2:
        await ctx.send("Please enter A and B amounts.\nExample: *gpa 35 3")
        print(f"{ctx.author} executed gpa (args length error)")
        return

    try:
        a = int(args[0])
        b = int(args[1])

        gpa = ((a*4)+(b*3))/(a+b)
        await ctx.send(f"Your GPA is {gpa}")
        print(f"{ctx.author} executed gpa (success)")
    except:
        await ctx.send("Please enter valid integer A and B amounts.\nExample: *gpa 35 3")
        print(f"{ctx.author} executed gpa (invalid args)")


@bot.command()
async def avi(ctx, member: discord.Member = None):
    if member is not discord.Member:
        await ctx.send(ctx.author.avatar_url)
        print(f"{ctx.author} executed avi (success) (no arg provided)")
    else:
        av = member.avatar_url
        await ctx.send(av)
        print(f"{ctx.author} executed avi (success)")


@bot.command(description="converts celsius to Fahrenheit", brief="*fahr [celsius value]", aliases=["toFahr", "tofahr"])
async def fahr(ctx, c=None):
    try:
        c = float(c)
        f = round((c*(9/5) + 32), 2)
        await ctx.send(f"{c} celsius is {f} Fahrenheit.")
        print(f"{ctx.author} executed fahr (success)")
    except:
        await ctx.send("Enter the value in celsius to convert it to Fahrenheit.")
        print(f"{ctx.author} executed fahr (error)")


@bot.command(description="converts Fahrenheit to celsius", brief="*cels [Fahrenheit value]", aliases=["toCels", "tocels"])
async def cels(ctx, f=None):
    try:
        f = float(f)
        c = round(((f - 32) * (5/9)), 2)
        await ctx.send(f"{f} Fahrenheit is {c} celsius.")
        print(f"{ctx.author} executed cels (success)")
    except:
        await ctx.send("Enter the value in Fahrenheit to convert it to celsius.")
        print(f"{ctx.author} executed cels (error)")


bot.run(token)
