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
        
    @commands.hybrid_group(fallback="foo")
    async def foo(self, ctx: commands.Context):
        """This is a hybrid command group."""
        await ctx.send("foo")

    # /foo bar | !foo bar
    @foo.command()
    async def bar(self, ctx: commands.Context):
        """This is a subcommand."""
        await ctx.send("bar")

    # /foo baz | !foo baz
    @foo.command()
    async def baz(self, ctx: commands.Context):
        """This is a regular command."""
        await ctx.send("baz")        

async def setup(bot):
    await bot.add_cog(SuperCog(bot))