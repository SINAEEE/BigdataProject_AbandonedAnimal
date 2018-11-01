from bs4 import BeautifulSoup
from urllib.parse import urlencode
import sys
from urllib.request import Request, urlopen
from datetime import datetime, timedelta
import math
import json
import pandas as pd
import os
import xmltodict

RESULT_DIRECTORY = '../__result__/crawling'

#동물관리보호소  공공데이터 API 서비스키

# SURVICE_KEY = 'lPho2AedT94HdWcuLEqLx%2FxutLFprTW4diIv6lp%2FylcbEtT0TFuMSfWdSiWip2LcqZ3fRfZ4tTKNyZiU%2BKUfAw%3D%3D'
SURVICE_KEY = 'kjzgwf40zX1dWlcX1PKEw2r%2BUfP1YbASnaMYa5dQ6aOr9mFJOi%2FcDQB%2FRlvaWdCVVQ5uSS%2BWwXU1WJYDAFmmBA%3D%3D'    # 김민규
# SURVICE_KEY = 'EdieVeGWBCgcq7f02Z4gpx%2FEssqE8l151SGr%2FHYps1SvWYKgXvpn35kSxTQUhMkxyf9yOrp2SU%2Fr9xZjf7aWQA%3D%3D'    # 송수진
# SURVICE_KEY = 'FXCllNPKHcV69y%2FBSMoNxmHKoCNvPRagdDMlScSRSsNJLbGqp12VchucwYzzGf1jWKNrbyi%2BBDF0zJSL%2Bi4K3Q%3D%3D'  # 김신애
base_url='http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic'


def animal_url(base=base_url, **params):
    url = '%s?%s&ServiceKey=%s' % (base, urlencode(params), SURVICE_KEY)
    return url

def animal_crawling():
        year = datetime.now().strftime('%Y')
        year = int(year)
        date = datetime.now().date()
        date = date - timedelta(days=1)
        date = str(date).split('-')

        # for year in range(2018):  # 년도가 바뀔 때마다, pageNo, isnext 초기화

        bgnde = '%s%s%s' % (date[0], date[1], date[2])  # 주소값 시작일
        endde = '%s%s%s' % (date[0], date[1], date[2])  # 끝일
        pageNo = 1
        isnext = True
        datalist = []
        columns = []
        encoding = 'utf-8'
        numOfRows = '1000'

        while isnext:
            url = animal_url(bgnde=bgnde, endde=endde, pageNo=pageNo, numOfRows=1)
            res = urlopen(url=url)

            if res is None:
                break

            xml_result = res.read().decode(encoding)
            xml_data = xmltodict.parse(xml_result)
            xml_dict = json.dumps(xml_data)
            dict_result = json.loads(xml_dict)
            xml_body = dict_result.get('response').get('body')
            xml_nor = None if dict_result is None else xml_body.get('numOfRows')
            xml_tc = None if dict_result is None else xml_body.get('totalCount')
            lostData = xml_body.get('items').get('item')
            print(lostData)

            # if len(columns)==0:
            #     for data in lostData.keys():
            #         columns.append(data)
            #

            datalist.append(lostData)


            cnt = math.ceil(int(xml_tc)/int(xml_nor))   # 크롤링 횟수 확인

            if pageNo == cnt:
                isnext = False
            else:
                pageNo += 1

        df = pd.DataFrame(datalist)     # Dict -> DataFrame
        df.to_csv('{0}/{1}_realtime_data.csv'.format(RESULT_DIRECTORY,bgnde),encoding='euc-kr',mode='w',index=True)



if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)

if __name__ == '__main__':

    animal_crawling()