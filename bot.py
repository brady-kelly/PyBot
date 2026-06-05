import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot_event_handler import BotEventHandler
from hybrid_commands import HybridCommands

load_dotenv()

TOKEN = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=discord.Intents.all())

events = BotEventHandler(bot)
hybrid = HybridCommands(bot)

async def setup_hook() -> None:  
    await bot.tree.sync()   

bot.setup_hook = setup_hook 

@bot.event
async def on_ready() -> None:
    await events.onReady()

@bot.hybrid_command()
async def ping(ctx: commands.Context) -> None:  
    await hybrid.ping(ctx)
    
bot.run(TOKEN)