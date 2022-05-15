import requests

class RiotApi(object):
    """https://developer.riotgames.com/

    Args:
        object (str): Riot API Key
        
    Samples:
        #print(riotApi.get_summoner_by_name('Admin Ben'))
        #print(riotApi.get_matches_by_name(puuid))
        #print(riotApi.get_matches_by_matchid('NA1_4167722674'))
    """
    
    def __init__(self, api_key: str, region="na1"):
        self.__RIOT_API_KEY = api_key
        self.__HEADER = {'X-Riot-Token': self.__RIOT_API_KEY}
        self.__REGION = region
        self.__ROUTING = "americas"
        self.__BASE_URL = ".api.riotgames.com/lol/"
        self.__API_URL_SUMMONER_V4 = "https://" + self.__REGION + self.__BASE_URL + "summoner/v4/summoners/"
        self.__API_URL_MATCH_V5 = "https://" + self.__ROUTING + self.__BASE_URL + "match/v5/matches/by-puuid/"
        self.__API_URL_MATCH_V5_MATCHID = "https://" + self.__ROUTING + self.__BASE_URL + "match/v5/matches/"

    def get_summoner_by_name(self, summoner_name: str) -> dict:
        """Summoner Infos and Ids
        @param summoner_name: LoL summoner name
        @return json object of infos and ids
        """
        
        url = self.__API_URL_SUMMONER_V4 + "by-name/" + summoner_name
        request = requests.get(url, headers=self.__HEADER)
        return request.json()

    def get_matches_by_name(self, puuid: str) -> dict:
        """Get summoner match history by name"""

        url = self.__API_URL_MATCH_V5 + puuid + "/ids"
        request = requests.get(url, headers=self.__HEADER)
        return request.json()

    def get_matches_by_matchid(self, matchid: str) -> dict:
        """Get matches by match id"""

        url = self.__API_URL_MATCH_V5_MATCHID + matchid
        request = requests.get(url, headers=self.__HEADER)
        return request.json()

    def get_summoner_by_puuid(self, puuid: str) -> dict:
        """Get summoner info by puuid"""

        url = self.__API_URL_SUMMONER_V4 + "by-puuid/" + puuid
        request = requests.get(url, headers=self.__HEADER)
        return request.json()

    #call
    def get_latest_matches_by_name(self, summoner_name:str) -> dict:
        """Latest match history info by summoner name"""

        return self.get_matches_by_matchid(self.get_matches_by_name(self.get_summoner_by_name(summoner_name)['puuid'])[0])