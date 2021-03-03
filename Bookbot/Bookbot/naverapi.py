import requests
import pandas as pd

def get_idpw():
    with open('C:/Users/dojun/Documents/api_keys/naver_api.txt') as f:
        client_id = f.readline().replace('\n', '')
        client_secret = f.readline()
    return client_id, client_secret

def search_title(keyword, nid, npw):
    url = 'https://openapi.naver.com/v1/search/book.json?query=' + keyword + '&display=30&start=1'
    html = requests.get(url, headers={"X-Naver-Client-Id": nid,
                                      "X-Naver-Client-Secret": npw})
    json1 = html.json()
    return json1['items']


def search_author(keyword, nid, npw):
    url = 'https://openapi.naver.com/v1/search/book_adv.json?d_auth=' + keyword + '&display=30&start=1'
    html = requests.get(url, headers={"X-Naver-Client-Id": nid,
                                      "X-Naver-Client-Secret": npw})
    json1 = html.json()
    return json1['items']

