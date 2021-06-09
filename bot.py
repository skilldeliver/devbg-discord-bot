import os

from discord.ext import commands


bot = commands.Bot(command_prefix='?')

bot.load_extension("cogs.example")

bot.run(os.environ["BOT_TOKEN"])
