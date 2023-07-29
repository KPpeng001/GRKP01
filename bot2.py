# This example requires the 'message_content' intent.

import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('안녕!'):
        await message.channel.send('어~ 그래그래 안녕?')

    if message.content.startswith('벌양!'):
        await message.channel.send('지금..벌레양반이라고 부른거지?')

    if message.content.startswith('벌레!'):
        await message.channel.send('아잇! 누구보고 벌레라고하는거야잇!')

    if message.content.startswith('좋은아침!'):
        await message.channel.send('어, 그래 썩 나쁘지않은 아침이지?')   

    if message.content.startswith('점심시간이에요'):
        await message.channel.send('자,자 아무리 바빠도 밥은 먹고 일해야지')

    if message.content.startswith('잘잤어요?'):
        await message.channel.send('어 그래 잘잤어?')
        
    if message.content.startswith('위로해줘'):
        await message.channel.send('오늘 하루도 고생 많았어')
        
    if message.content.startswith('잘자요'):
        await message.channel.send('그래그래, 잘자~<하~품>')        

    if message.content.startswith('사는게 힘들어요'):
        await message.channel.send('사는게 다 힘들지... 지옥이나 다름없는 삶이겠지만 살아가줘')

    if message.content.startswith('아저씨 뚱뚱해요?'):
        await message.channel.send('어? 나 뚱뚱해?')            


access_token = os. environ["Bot_TOKEN"]
client.run('assess_TOKEN')
