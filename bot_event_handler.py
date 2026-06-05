class BotEventHandler:

    def __init__(self, bot) -> None:
        self.bot = bot

    async def onReady(self):
        print(f"Logged in as {self.bot.user}")