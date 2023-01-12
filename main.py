import os
import discord
from discord.ext import commands
import requests
import json
import random  

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.message_content = True
#intents.content = True
#intents.members = true


client = discord.Client(intents=intents)



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!ink hello'):
    await message.channel.send('Hello World!')
  if message.content.startswith('!ink goodbye'):
    await message.channel.send('Goodbye Cruel World!')  

client.run(os.environ['TOKEN'])

