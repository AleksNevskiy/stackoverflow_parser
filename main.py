from pprint import pprint
import requests

def  stackoverflow_parser():
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'order': 'desc', 'sort': 'activity', 'site': 'stackoverflow', 'fromdate': 1293840000, 'todate': 1635496221, 'tagged': 'Python'}
    response = requests.get(url=url, params=params)
    return response.json()



if __name__ == '__main__':
    pprint(stackoverflow_parser())