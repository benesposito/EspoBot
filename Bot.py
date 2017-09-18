import discord
import asyncio
from random import randint

client = discord.Client()

async def getTeams(message):
    players = message.content.split(" ")
    print(len(players))
    if len(players) == 1:
        players = [""]

        channel = message.author.voice.voice_channel

        for p in channel.voice_members:
            players.append(p.name)

    print(players)
    team = randint(0, 1)
    team1 = []
    team2 = []
    for i in range(len(players) - 1, 0, -1):
        print(players[i])
        rand = randint(0, i)

        if team:
            team1.append(players[i])
        else:
            team2.append(players[i])

        team = not team
    return [team1, team2]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('>teams'):
        teams = await getTeams(message)

        await client.send_message(message.channel, teams[0])
        await client.send_message(message.channel, teams[1])

client.run('MzU5MDA3MjQyOTI3ODY1ODU2.DKAxKA.GfC1o7Qp4vmqsweCjXu0bVb9oSI')
