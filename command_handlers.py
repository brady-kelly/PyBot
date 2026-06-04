import random


class BotCommandHandler:
    
    def __init__(self, guild, bot) -> None:
        self.guild = guild
        self.bot = bot
                
    def onReady(self):
        print(f'{self.bot.user.name} has connected to Discord!')
        
    async def nineNine(self, ctx):
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)