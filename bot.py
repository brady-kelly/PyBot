# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from command_handler import BotCommandHandler
from error_handler import BotErrorHandler
from event_handlers import ClientEventHandler
from discord.ext import commands

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

comms = BotCommandHandler(GUILD, bot)
errs = BotErrorHandler(GUILD, bot)

@bot.event
async def on_ready():
    comms.onReady()

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    print("command")
    await comms.nineNine(ctx)
    
@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    await comms.roll(ctx, number_of_dice, number_of_sides)
    
@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name=''):
    await comms.createChannel(ctx, channel_name)
        
@bot.event
async def on_command_error(ctx, error):
    await errs.onCommandError(ctx, error)       

bot.run(TOKEN)