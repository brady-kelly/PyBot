import random

import discord

class ClientEventHandler:

    def __init__(self, guild, client) -> None:
        self.guild = guild
        self.client = client

    def onReady(self):
        
        guild = discord.utils.get(self.client.guilds, name=self.guild)
        if guild is not None:
            print(
                f'{self.client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
        else:
            print(f"Warning: Could not find a guild matching '{self.guild}'")
            
    async def onMemberJoin(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
        )
        print(f'{member.name}, has joined!')
        
    async def onMessage(self, message):
        if message.author == self.client.user:
            return

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)   
        elif message.content == 'raise-exception':
            raise discord.DiscordException     
        
    async def onError(self, event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise