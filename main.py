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
    print(f"{ctx.author} executed ping") # for showing what command is executed by who


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


@bot.command(description="returns a user's avi", brief="*avi [user]", aliases=["avatar", "ava"])
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


@bot.command(description="converts kilograms to pounds", brief="*pound [kilogram value]", aliases=["lb", "pounds"])
async def pound(ctx, kg=None):
    try:
        lb = round((float(kg) * 2.205), 3)

        await ctx.send(f"{kg} kilogram(s) ≈ {lb} pound(s).")
        print(f"{ctx.author} executed pound (success)")
    except:
        await ctx.send("Enter a kilogram value to convert it to pounds.")
        print(f"{ctx.author} executed pound (error)")


@bot.command(description="converts pounds to kilograms", brief="*kilo [pound value]", aliases=["kg", "kilogram", "kilos", "kilograms"])
async def kilo(ctx, lb=None):
    try:
        kg = round((float(lb) / 2.205), 3)

        await ctx.send(f"{lb} pound(s) ≈ {kg} kilogram(s).")
        print(f"{ctx.author} executed kilo (success)")
    except:
        await ctx.send("Enter a pound value to convert it to kilograms.")
        print(f"{ctx.author} executed kilo (error)")


@bot.command(description="Plays rock, paper, scissors", brief="*rps [choice]", aliases=["rockpaperscissors"])
async def rps(ctx, choice=""):
    emojis = {
        "rock": "🪨",
        "paper": "🧻",
        "scissors": "✂️",
    }

    choice = choice.lower()
    if choice != "rock" and choice != "paper" and choice != "scissors":
        choice = random.choice(["rock", "paper", "scissors"])
        await ctx.send(f"Invalid input. Your randomly chosen input is {choice} {emojis[choice]}.")

    comp = random.choice(["rock", "paper", "scissors"])

    results = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if results[choice] == comp:
        await ctx.send(f"You won! \nThe computer chose {comp} {emojis[comp]}. \n{emojis[choice]} > {emojis[comp]}")
    elif results[comp] == choice:
        await ctx.send(f"You lost! \nThe computer chose {comp} {emojis[comp]}. \n{emojis[choice]} < {emojis[comp]}")
    else:
        await ctx.send(f"It's a draw! \nThe computer chose {comp} too {emojis[comp]}. \n{emojis[choice]} = {emojis[comp]}")

    print(f"{ctx.author} executed rps (success)")



bot.run(token) # token from config.json
