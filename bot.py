import os
from decouple import config
from discord.ext import commands
import discord

#intents = discord.Intents.default()
#intents = discord.Intents.all()
#intents.members = True

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# bot = commands.Bot("!")

def load_cogs(bot):
    bot.load_extension("manager")
    bot.load_extension("tasks.dollartoReal")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")

load_cogs(bot)

TOKEN = config("TOKEN_SECRET")
bot.run(TOKEN)





