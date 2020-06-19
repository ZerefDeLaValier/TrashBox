import os
import random
import discord


client = discord.Client()
prefix = "$"

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    answr = message.content.lower()
    if answr == "ping":
        response = "pong"
        await message.channel.send(response)
    if answr == "геи":
        response = "Осуждаю"
        await message.channel.send(response)
@client.event
async def on_message_delete(message):
    print(message.id)
    response = message.content
    print("Debug")
    await message.channel.send(response)
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}, welcome! Why are you gay?'
    )

client.run("NTUxNzY3NDY3NDM3OTgxNzM2.D117Cw.hg6n-WmE-tBzK8BHj9tSWJztqdk")