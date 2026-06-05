class HybridCommands:
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    async def ping(self, ctx):
        await ctx.send(f"> Pong! {round(self.bot.latency * 1000)}ms")