import json
import os, os.path
import pandas as pd
from visibleAreaMethods import getBottomRightCoord, getTopLeftCoord

# load matches from individual seasons
allSeasons = []

for dir in os.listdir('data/matches'):
    for f in os.listdir('data/matches/'+dir):
        with open('data/matches/'+dir+'/'+f) as season:
            seasonDict = json.load(season)
            allSeasons.append(seasonDict)

allMatches = []

for season in allSeasons:
    for match in season:
        allMatches.append(match)

matchesDF = pd.DataFrame(allMatches)
# clean dataframe
matchesDF = matchesDF.fillna("")
matchesDF["match_date"] = pd.to_datetime(matchesDF["match_date"], format='ISO8601') 
matchesDF["last_updated"] = pd.to_datetime(matchesDF["last_updated"], format='ISO8601') 
matchesDF["last_updated_360"] = pd.to_datetime(matchesDF["last_updated_360"], format='ISO8601')
matchesDF = matchesDF.drop(columns="kick_off")

#set up 360 data
allThreeSixty = []

for file in os.listdir('data/three-sixty'):
    with open('data/three-sixty/'+file, 'r') as event:
        try:
            eventDict = json.load(event)
            allThreeSixty.append(eventDict)
        except:
            with open("panda_360_unread.txt", 'a') as log:
                    log.write('data/three-sixty/'+file+'\n')

#create list of matches
threeSixtyDF = [pd.DataFrame(event) for event in allThreeSixty]
threeSixtyDF[0].info()

def to_list(x):
    if isinstance(x, list):
        return x
    
#convert cols to py type
for match in threeSixtyDF:
    columnVA = match["visible_area"]
    columnFF = match["freeze_frame"]
    for row in columnVA:
        row = to_list(row)
    for row in columnFF:
        row = to_list(row)

match = threeSixtyDF[0]
print(getTopLeftCoord(match))
print(getBottomRightCoord(match))