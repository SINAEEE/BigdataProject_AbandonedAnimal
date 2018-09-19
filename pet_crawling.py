import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import csv
import numpy as np
# 서비스토큰
Servicekey='kjzgwf40zX1dWlcX1PKEw2r%2BUfP1YbASnaMYa5dQ6aOr9mFJOi%2FcDQB%2FRlvaWdCVVQ5uSS%2BWwXU1WJYDAFmmBA%3D%3D'
# # url
# url ='http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/kind?up_kind_cd=417000&ServiceKey='+Servicekey
# # url에서 정보를 받아옴
# res=requests.get(url=url)
# # url에서 받아온 정보를 res에 저장하고 text형태로 불러와 plain_text에 저장
# plain_text=res.text
# #print(plain_text,'오징어다')
# # text값을 html형식으로 변경
# dog = BeautifulSoup(plain_text, 'lxml' )
#
# dogName = dog.findAll('knm')
# dogtag = dog.findAll('kindcd')
#
# dtlist=[]
# for string in dogtag:
#     #print(string.string)
#     dtlist.append(string.string)
#
#
# dnlist=[]
# for string in dogName:
#     #print(string.string)
#     dnlist.append(string.string)
#
# dogdata = list(zip(dnlist,dtlist))
# print(dogdata)





base_url='http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?bgnde=20180101&endde=20180901&pageNo=1&numOfRows=1000&ServiceKey='+Servicekey
res = urlopen(url=base_url)
print(res.url)
datalist = []
for i in range (1,100):
    pageNo=i
    url=base_url.format(pageNo)
    res = urlopen(url=url)
    soup=BeautifulSoup(res,'lxml')
    lostData = soup.findAll('item')
    print(lostData)
    for ld in list(lostData):
        c = list(ld.strings)
        datalist.append(c)

     print(datalist)

df = pd.DataFrame(datalist)
print(df)

df.to_csv('lostanimals.csv', mode='w', encoding='EUC-KR')
