# 중복 확인 및 중복제거
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import time
import shutil # pip install shutil
import os
import sys

Keyword = input("검색어를 입력하세요: ")
count_down = int(input("스크롤 다운 횟수를 입력해 주세요(최대6): "))

driver = webdriver.Chrome('C:/Python_data/chromedriver.exe')
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
driver.get(url+Keyword)

img_url_lst = []

for count in range(count_down):
    # 더보기 버튼 클릭
    #driver.find_element_by_css_selector('#_sau_imageTab > div > div.more_img > a').click()
    # 구조변경 210113 확인
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # 크롬드라이버가 열어 놓은 html문서 소스 가지고 온 후 'html.parser'
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    tag_img = soup.find_all("div",class_='thumb')
    for url_num in tag_img:
        img_url_lst.append(url_num.find('img')['src'])
    
# 중복 url제거    
img_url_lst = set(img_url_lst)

# img_url_lst에 있는 url들에 접속하여 이미지 저장
fdir = 'c:/Python_data/'
gen_fname = Keyword+'네이버크롤'

# 저장 디렉토리 만들기
list_dir = os.listdir(fdir)
for fname in list_dir:
    if gen_fname == fname:
        ck = input("동일한 이름의 폴더가 있습니다. 삭제 할까요>[y/n]")
        if ck =='y' or ck =='ㅛ':
            shutil.rmtree(fdir+gen_fname)
        elif ck =='n' or ck == 'ㅜ':
            gen_fname = input("새로 생성할 폴더 이름을 입력하세요: ")
        else:
            print("잘못 누르셨습니다.")
            print("프로그램을 종료합니다.")
            driver.close()
            sys.exit()
try: 
    os.makedirs(fdir+gen_fname)
except FileExistsError:
    gen_fname = input("동일한 폴더명이 있습니다 새로 입력해 주세요: ")
    os.makedirs(fdir+gen_fname)
    
# 동일한 폴더명이 있으면 지워주거나 새로이름을 지정해 줘야한다.
i = 0
for img_url in tqdm(img_url_lst,desc='img saving...'):
    # URL내용 저장: urllib.request.urlretrieve("url주소", '파일경로.확장자')
    img_name = fdir+gen_fname+'/'+Keyword+str(i)+'.jpg'
    urllib.request.urlretrieve(img_url, img_name)
    i += 1
driver.close()
print('완료 총',len(img_url_lst),'개의 이미지를 저장 했습니다.')