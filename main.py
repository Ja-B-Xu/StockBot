import requests
import json
import tda


td_key = ''


account_num = ''

def getTokens(): #unfinished
    endpoint = 'https://api.tdameritrade.com/v1/oauth2/token'

    payload = {'grant_type': 'authorization_code',
               'access_type': 'offline',
               'code': post_access_code,
               'client_id': td_key+"@AMER.OAUTHAP",
               'redirect_uri': 'http://localhost'}

    content = requests.get(url=endpoint, params=payload)

    data = content.json()
    print(data)

def getPriceHistory(ticker):
    endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(ticker)

    payload = {'apikey': td_key,
               'periodType': 'day',
               'period': '2',
               'frequencyType': 'minute',
               'frequency': '30',
               'needExtendedHoursData': 'true'
               }

    content = requests.get(url = endpoint, params = payload)

    data = content.json()
    print(data)

def getQuote(ticker):
    endpoint = r'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(ticker)

    payload = {'apikey': td_key}

    content = requests.get(url = endpoint, params = payload)

    data = content.json()
    print(data)

def getAccount(query): #unfinished
    endpoint = r'https://api.tdameritrade.com/v1/accounts/{}'.format(account_num)

    payload = {'apikey': td_key,
               'fields': query}

    content = requests.get(url=endpoint, params=payload)

    data = content.json()
    print(data)


getQuote('GME')