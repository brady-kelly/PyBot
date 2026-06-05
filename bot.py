# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from command_handlers import BotCommandHandler
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
    
@bot.command(name='channel-new')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='newchan'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)    
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')        

bot.run(TOKEN)