from discord.ext import commands

class BotErrorHandler:
    
    def __init__(self, guild, bot) -> None:
        self.guild = guild
        self.bot = bot
        
    async def onCommandError(self, ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have the correct role for this command.')   