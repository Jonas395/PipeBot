import json
import discord
import random
import threading

fconfig = open('config.json', 'r')
config = json.load(fconfig)
fconfig.close()

activity = discord.Game(name="with ur mailbox")

intents = discord.Intents.default()
intents.message_content = True

threadStarted = False
client = discord.Client(intents=intents)

def play_pipe():
    source = discord.FFmpegPCMAudio(executable="C:/FFmpeg/ffmpeg.exe", source="pipe.mp3")
    vClient.play(source)
    if vClient.is_connected():
        threading.Timer(random.randrange(15, 500), play_pipe).start()
                        
@client.event
async def on_ready(): 
    print(f'Logged on as{client.user}')
    
@client.event
async def on_message(message):
    global threadStarted, vClient
    if message.content.startswith('|') and threadStarted is False:
        threadStarted = True
        vChannel = message.author.voice.channel
        vClient = await vChannel.connect()
        vClient.stop()
        threading.Timer(random.randrange(15, 500), play_pipe).start()

client.run(config['token'])