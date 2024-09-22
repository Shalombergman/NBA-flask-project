

# NBA_API_URL = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"
# DATA_ALL_PLAYERS = "PlayerDataAdvancedPlayoffs"
# SEASONS = ['2022','2023','2024']
#
# def get_players_from_nba_api(SEASONS:str)-> object:
#     response = requests.get(f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={SEASONS}&&pageSize=10000000000000")
#     print(response)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(response.status_code)
#         return None
# print(get_players_from_nba_api('2024'))

import requests



a = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={}&pageSize=10000000000000"
NBA_API_URL = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={''}&pageSize=1000"
SEASONS = ['2022', '2023', '2024']

def get_players_from_nba_api(season):
    response = requests.get(NBA_API_URL.format(season))

    if response.status_code == 200:

        return response.json()

    else:
        print(f"Error fetching data: {response.status_code}")
        return None
# print(get_players_from_nba_ap_from_nba_api(SEASONS[0]))
