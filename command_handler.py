import random
import discord

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
        
    async def roll(self, ctx, number_of_dice, number_of_sides):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))
        
    async def createChannel(self, ctx, channel_name):
        if channel_name == '':
            await ctx.send('Channel name is missing')
            return
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)                        