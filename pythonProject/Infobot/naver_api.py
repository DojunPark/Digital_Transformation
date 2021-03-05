import requests
from bs4 import BeautifulSoup as bs
import re

def n_get_idpw():
    with open('C:/Users/dojun/Documents/api_keys/naver_api.txt') as f:
        client_id = f.readline().replace('\n', '')
        client_secret = f.readline()
    return client_id, client_secret

def n_book_title(keyword, nid, npw):
    url = 'https://openapi.naver.com/v1/search/book.json?query=' + keyword + '&display=30&start=1'
    html = requests.get(url, headers={"X-Naver-Client-Id": nid,
                                      "X-Naver-Client-Secret": npw})
    json1 = html.json()
    return json1['items']


def n_book_author(keyword, nid, npw):
    url = 'https://openapi.naver.com/v1/search/book_adv.json?d_auth=' + keyword + '&display=30&start=1'
    html = requests.get(url, headers={"X-Naver-Client-Id": nid,
                                      "X-Naver-Client-Secret": npw})
    json1 = html.json()
    return json1['items']


def n_movie_title(keyword, nid, npw):
    url = 'https://openapi.naver.com/v1/search/movie.json?query=' + keyword + '&display=30&start=1'
    html = requests.get(url, headers={"X-Naver-Client-Id": nid,
                                      "X-Naver-Client-Secret": npw})
    json1 = html.json()
    return json1['items']


def n_movie_rank():
    url = 'https://movie.naver.com/movie/running/current.nhn#'
    html = requests.get(url)
    soup = bs(html.content, 'html.parser')

    panel = soup.find('ul', class_='lst_detail_t1')
    movies = panel.find_all('li')

    infos = []
    for movie in movies:
        img = movie.find('img')
        title = movie.find('dt', class_='tit').find('a').text
        point = movie.find('dl', class_='info_star').find('span', class_='num').text
        box = movie.find('dl', class_='info_txt1').find_all('span', class_='link_txt')
        director = re.sub('\n|\t|\r', '', box[-2].text)
        actor = re.sub('\n|\t|\r', '', box[-1].text)

        infos.append((img, title, point, director, actor))

    return infos


def n_shopping_title(keyword, nid, npw):
    url = 'https://openapi.naver.com/v1/search/shop.json?query=' + keyword + '&display=30&start=1'
    html = requests.get(url, headers={"X-Naver-Client-Id": nid,
                                      "X-Naver-Client-Secret": npw})
    json1 = html.json()
    return json1['items']