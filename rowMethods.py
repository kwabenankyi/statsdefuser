def numberOfTeammatesInFrame(frame):
    count = 0
    for player in frame:
        if player["teammate"]:
            count += 1
    return count

def numberOfOpponentsInFrame(frame):
    count = 0
    for player in frame:
        if not player["teammate"]:
            count += 1
    return count

def numberOfPlayersInFrame(frame):
    return len(frame)

def homeAveragePosition(frame):
    count = numberOfTeammatesInFrame(frame)
    x, y = 0
    for player in frame:
        if player["teammate"]:
            x += player["location"][0]
            y += player["location"][1]
    return [x/count, y/count]

def awayAveragePosition(frame):
    count = numberOfOpponentsInFrame(frame)
    x, y = 0
    for player in frame:
        if not player["teammate"]:
            x += player["location"][0]
            y += player["location"][1]
    return [x/count, y/count]