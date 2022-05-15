from RiotApi import RiotApi
from dotenv import load_dotenv
import os

def get_lol_stats(summonerName):
    load_dotenv()
    riotApi = RiotApi(os.getenv('RIOT_API_KEY'))

    match = riotApi.get_latest_matches_by_name(summonerName)
    matchId = match['metadata']['matchId']
    gameDuration = match['info']['gameDuration']
    gameMode = match['info']['gameMode']
    gameType = match['info']['gameType']

    for participant in match['info']['participants']:
        #if a list of participant names...
        if participant['summonerName'] == summonerName:
            #general
            summonerLevel = participant['summonerLevel']
            championName = participant['championName']
            win = participant['win']

            #economy
            goldEarned = participant['goldEarned']
            goldSpent = participant['goldSpent']

            #KDA
            kills = participant['kills']
            deaths = participant['deaths']
            assists = participant['assists']

            #double triple quadra penta kill
            doubleKills = participant['doubleKills']
            tripleKills = participant['tripleKills']
            quadraKills = participant['quadraKills']
            pentaKills = participant['pentaKills']

            break

    print('matchId: {}\ngameDuration: {}\ngameMode: {}\ngameType: {}\n \
        summonerLevel: {}\nchampionName: {}\nwin: {}\n \
        goldEarned: {}\ngoldSpent: {}\n \
        kills: {}\ndeaths: {}\nassists: {}\n \
        doubleKills: {}\ntripleKills: {}\nquardraKills: {}\npentaKills: {}'.format(matchId, gameDuration, gameMode, gameType, summonerLevel, championName, win, goldEarned, goldSpent, kills, deaths, assists, doubleKills, tripleKills, quadraKills, pentaKills))

    '''print('\n')
    for participant in match['metadata']['participants']:
        print('participant: {}\n'.format(riotApi.get_summoner_by_puuid(participant)))'''
    
def main():
    get_lol_stats('Admin Ben')
    
if __name__ == '__main__':
    main()