import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?devbg'):
        await message.channel.send('Най-голямата IT общност в България. - https://dev.bg/')

client.run(os.environ["BOT_TOKEN"])