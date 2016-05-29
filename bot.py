''' The main file for the bot '''
import os
import sys
import json
import discord
from discord import opus

with open('bot.json') as data:
    CONFIG = json.load(data)

client = discord.Client(max_messages=100)

@client.event
async def on_ready():
    ''' Executed when the bot successfully connects to Discord. '''
    print('Logged in!\nName: {}\nId: {}'.format(client.user.name, client.user.id))
    if sys.maxsize > 2**32:
        opus.load_opus('libopus-0.x64.dll')
    else:
        opus.load_opus('libopus-0.x86.dll')

@client.event
async def on_message(msg):
    ''' Executed when a message is posted to a server '''
    if msg.author.id != client.user.id: # ignore our own commands
        if msg.content.startswith(CONFIG['invoker']):
            g_1 = msg.content.lower()[len(CONFIG['invoker']):]
            if g_1 == 'help':
                g_4 = '\n' + CONFIG['invoker']
                g_3 = '{0}git\n{0}{1}'.format(CONFIG['invoker'], g_4.join(os.listdir('sound/')))
                g_3 = g_3.lower().replace(CONFIG['fileformat'], '')
                g_2 = 'Commands for ' + CONFIG['bot'] + ':\n' + \
                          g_3 + '\nYou must be in a voice channel for this to work.'
                if not msg.channel.is_private:
                    await client.send_message(msg.channel, 'Sending a DM of commands...')
                await client.send_message(msg.author, g_2)
            elif g_1 == 'git':
                await client.send_message(msg.channel, 'https://github.com/lilpea/simplesoundbot')
            else:
                if msg.author.voice_channel:
                    try:
                        voice = await client.join_voice_channel(msg.author.voice_channel)
                        player = voice.create_ffmpeg_player('sound/' + g_1 + CONFIG['fileformat'])
                        player.start()
                    except:
                        pass
                else:
                    await client.send_message(msg.channel, 'You\'re not in a voice channel!')
                while True:
                    try:
                        if player.is_done():
                            await voice.disconnect()
                            break
                    except:
                        break

client.run(CONFIG['token'])
