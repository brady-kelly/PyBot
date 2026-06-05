import logging

import discord
from discord.ext import commands

class SuperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(self.__class__.__name__)
        
    @commands.hybrid_command()
    async def ping(self, ctx):
        await ctx.send(f"> Pong! {round(self.bot.latency * 1000)}ms")
        
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        self.logger.info(f"message from {message.author}: {message.content}")        

async def setup(bot):
    await bot.add_cog(SuperCog(bot))