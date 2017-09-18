from random import randint

async def getTeams(message):
    players = message.content.split(" ")

    if len(players) == 0:
        players = []

        channel = message.author.voice.voice_channel

        for p in channel.voice_members:
            players.append(p.name)

    team = randint(0, 1)
    team1 = []
    team2 = []
    for i in range(len(players) - 1, 0, -1):
        rand = randint(0, i)

        if team:
            team1.append(players[i])
        else:
            team2.append(players[i])

        team = not team
    return [team1, team2]

players = ["ben", "nick", "joe", "john", "noah", "donovon", "tommy", "brayden"]

teams = getTeams(players)
team1 = teams[0]
team2 = teams[1]

print(team1)
print(team2)
