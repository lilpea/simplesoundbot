''' First-time setup '''
import os
import json
import discord
import time

with open('bot.json') as data:
    CONFIG = json.load(data)

client = discord.Client(max_messages=100)

@client.event
async def on_ready():
    ''' Setup '''
    if os.path.isfile('avy.png'):
        await client.edit_profile(avatar=open('avy.png', 'rb').read())
    elif os.path.isfile('avy.jpg'):
        await client.edit_profile(avatar=open('avy.jpg', 'rb').read())
    else:
        await client.edit_profile(avatar=open('def.png', 'rb').read())
    print('Ready! (you can open \'run bot.bat\' now)')
    time.sleep(10)
    quit()

client.run(CONFIG['token'])
