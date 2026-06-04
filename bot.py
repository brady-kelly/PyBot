# bot.py
import os
import random

import discord
from dotenv import load_dotenv

from handlers import ClientEventHandler

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)
handler = ClientEventHandler(GUILD, client)

@client.event
async def on_ready():
    handler.onReady()
        
@client.event
async def on_member_join(member):
    await handler.onMemberJoin(member)

@client.event
async def on_message(message):
    await handler.onMessage(message)
    
@client.event
async def on_error(event, *args, **kwargs):
    await handler.onError(event, args, kwargs)

client.run(TOKEN)