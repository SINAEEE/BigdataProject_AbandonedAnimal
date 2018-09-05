from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlencode
import math
import xml
import pandas as pd

SURVICE_KEY = 'kjzgwf40zX1dWlcX1PKEw2r%2BUfP1YbASnaMYa5dQ6aOr9mFJOi%2FcDQB%2FRlvaWdCVVQ5uSS%2BWwXU1WJYDAFmmBA%3D%3D'    # 김민규
# SURVICE_KEY = 'EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D'    # 송수진
# SURVICE_KEY = 'FXCllNPKHcV69y%2FBSMoNxmHKoCNvPRagdDMlScSRSsNJLbGqp12VchucwYzzGf1jWKNrbyi%2BBDF0zJSL%2Bi4K3Q%3D%3D'  # 김신애
base_url='http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic'
# bgnde=20180101&endde=20180901&pageNo=1&numOfRows=10&ServiceKey=


def animal_url(base=base_url, **params):
    url = '%s?%s&ServiceKey=%s' % (base, urlencode(params), SURVICE_KEY)
    return url




for year in range(2017, 2019):
    bgnde = '%s0101' % (year)
    endde = '%s1231' % (year)
    pageNo = 1
    isnext = True
    datalist = []

    while isnext:
        url = animal_url(bgnde=bgnde, endde=endde, pageNo=pageNo, numOfRows=1000)
        res = urlopen(url=url)

        if res is None:
            break

        xml_result = BeautifulSoup(res, 'xml')

        xml_body = xml_result.find('body')
        xml_nor = None if xml_result is None else xml_body.find('numOfRows')
        xml_tc = None if xml_result is None else xml_body.find('totalCount')

        lostData = xml_body.findAll('item')

        for data in list(lostData):
            c = list(data.strings)
            datalist.append(c)

        nor = list(xml_nor.strings)
        tc = list(xml_tc.strings)
        print(tc)

        cnt = math.ceil(int(tc[0])/int(nor[0]))

        if pageNo == cnt:
            isnext = False
        else:
            pageNo += 1

        df = pd.DataFrame(datalist)
        print(df)

    filename = 'lostAnimal_%s_%s.csv' % (bgnde, endde)
    df.to_csv(filename, mode='w', encoding='euc-kr')