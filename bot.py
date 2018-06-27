import discord
from discord.ext import commands
import logging
import traceback



logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix='d.')
bot.remove_command('help')
