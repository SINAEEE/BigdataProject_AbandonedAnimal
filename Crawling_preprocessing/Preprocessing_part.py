from bs4 import BeautifulSoup
from urllib.parse import urlencode
import sys
from urllib.request import Request, urlopen
from datetime import datetime, timedelta
import math
import json
import os
import xmltodict
import pandas as pd
import re
import pymysql
from sqlalchemy import create_engine

# df=pd.read_csv('D:/PycharmProject/IntroducePython/__result__/crawling/20181107_realtime_data.csv',encoding="euc-kr")
# df=df.drop("Unnamed: 0",1)
# df=df.fillna("NaN")
RESULT_DIRECTORY = '../__result__/crawling'

def db_save():
    # year = datetime.now().strftime('%Y')
    # year = int(year)
    # date = datetime.now().date()
    # date = date - timedelta(days=1)
    # date = str(date).split('-')
    # bgnde = '%s%s%s' % (date[0], date[1], date[2])  # 주소값 시작일

    df = pd.read_csv('{0}/{1}.csv'.format(RESULT_DIRECTORY,'lostAnimal_20180907_20181108' ), encoding="euc-kr")
    df = df.drop("Unnamed: 0", 1)
    df = df.fillna("NaN")

    # ------------------------------------------- 컬럼을 리스트로 변환
    a = [df.loc[i, j] for i in df.index for j in df[['weight']]]
    b = [df.loc[i, j] for i in df.index for j in df[['age']]]

    temp_weight = []
    temp_age = []

    # ------------------------------------ weight 에러단어만 검출
    for i in a:
        pattern = re.compile(r'\d[.]\d\(Kg\)+|\d\(Kg\)+|\d\d\(Kg\)+|\d?\d[.]\d?\d?\(Kg\)')  # 형식에 맞는 패턴 인식
        no_error_weight_word = pattern.findall(i)  # 패턴값과 맞는 값을 반환
        temp_weight += no_error_weight_word  # 임시리스트에 추가
    error_word_weight = list(set(a) - set(temp_weight))  # 차집합
    print(temp_weight)
    print(no_error_weight_word, '\n')

    print("임시 weight 리스트 반환\n")
    print(temp_weight, '\n')

    print("임시 에러weight 초기화\n")
    del temp_weight[:]
    print(temp_weight)

    print(error_word_weight)

    # ------------------------------------ age 에러단어만 검출
    for j in b:
        pattern2 = re.compile(r'20+[0-1]+[0-9]\(년생\)')  # 형식에 맞는 패턴 인식
        no_error_age_word = pattern2.findall(j)  # 패턴값과 맞는 값을 반환
        temp_age += no_error_age_word  # 임시리스트에 추가
    error_word_age = list(set(b) - set(temp_age))  # 차집합
    print(no_error_age_word, "패턴값 반환")
    print(temp_age, "임시 age 리스트 반환")
    del temp_age[:]
    print(temp_age, "임시 에러age 초기화")
    print(error_word_age)
    conn = pymysql.connect(host='localhost', user='root', password='mkyu0917', db='animaldb', charset='utf8mb4', )
    curs = conn.cursor()
    # -----------------------테이블이 없을시에 테이블 생성

    SQL_QUERY = '''
               CREATE TABLE IF NOT EXISTS animaldb.weight_error(
                   id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
                   weight VARCHAR(30) NOT NULL,
                   PRIMARY KEY(id)
                   )DEFAULT CHARSET=utf8mb4 '''
    SQL_QUERY2 = """
        CREATE TABLE IF NOT EXISTS animaldb.age_error(
            id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
            age VARCHAR(30) NOT NULL,
            PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 
        """

    curs.execute(SQL_QUERY)
    conn.commit()

    curs.execute(SQL_QUERY2)
    conn.commit()

    # === 에러단어만 각 테이블에 insert ===

    sql1 = """insert into age_error(age) values (%s)"""
    sql2 = """insert into weight_error(weight) values (%s)"""

    # === 에러단어만 들어있는 리스트를 통채로 db에 적재 ===
    curs.executemany(sql1, error_word_age)
    conn.commit()

    curs.executemany(sql2, error_word_weight)
    conn.commit()

    # === 적제된 에러문자의 데이터를 select문으로 불러옴
    sql_a = """ select * from weight_error """
    sql_b = """ select * from age_error"""

    curs.execute(sql_a)
    result_weight_error = curs.fetchall()
    print(result_weight_error, "db_weight 에러단어\n")

    curs.execute(sql_b)
    result_age_error = curs.fetchall()
    print(result_age_error, "db_age 에러단어\n")

    list_temp = []  # weight에러가 있는 로우가 들어갈 리스트
    list_temp2 = []  # weight,age오류가 없는 로우가 들어갈 리스트

    # ------불러온 에러단어리스트 속 튜플에서 속성값 i값의 1번째를 가져옴
    if len(result_weight_error) != 0:
        for i in result_weight_error:
            error = i[1]
            for j in df.itertuples():

                if j.__contains__(error):
                    list_temp.append(j)
                else:
                    list_temp2.append(j)

        list_temp2 = list(set(list_temp2))
    else:
        for j in df.itertuples():
            list_temp2.append(j)

        list_temp2 = list(set(list_temp2))
        print("weight 에러단어가 없습니다.")
        # print(list_temp2,'에러없는 데이터')
        # print(list_temp,'에러있는 데이터')

    if len(result_age_error) != 0:
        for i in result_age_error:
            error = i[1]
            for j in list_temp2:

                if j.__contains__(error):
                    list_temp.append(j)
    else:
        print("age에러단어가 없습니다.")

    engine = create_engine("mysql+pymysql://root:" + "mkyu0917" + "@localhost:3306/animaldb?charset=utf8mb4",
                           encoding='utf8')
    conn = engine.connect()

    if len(set(list_temp)) != 0:
        realdata = list(set(list_temp2) - set(list_temp))
    else:
        realdata = list(set(list_temp2))
        print(realdata)

    if len(set(list_temp)) != 0:
        error_df = pd.DataFrame(list_temp).drop('Index', 1).drop_duplicates()  # index 컬럼제거 row중복값 제거
        print("error_df", error_df)
        error_df.to_sql(name='animal_realtime_2018_error', con=engine, if_exists='append', index=False)
        del error_df
    else:
        print("에러데이터가 없기때문에 저장하지 않습니다.")

    if len(realdata) != 0:


        no_error_df = pd.DataFrame(realdata).drop('Index', 1).drop_duplicates()  # index 컬럼제거 row중복값 제거
        print("에러가 없는 데이터를 저장했습니다.", no_error_df)


        # ---------------전처리 시작하는 부분----------------#
        #----------age 전처리-------------------------------
        no_error_df['age(before)'] = no_error_df["age"].copy(deep=True)
        no_error_df['age(after)'] = no_error_df['age'].copy(deep=True)

        list_age = []
        ages = no_error_df["age(after)"]
        for i in ages:
            parse = re.sub('\(년생\)', '', i)
            age = abs(int(parse) - int(2018))
            list_age.append(age)

        no_error_df['age(after)'] = list_age



        #### (processState, sexCd, neuterYn) 전처리(레이블링, column화, one-hot 코딩)

        no_error_df['processState_og']=no_error_df['processState'].copy(deep='True')
        no_error_df.loc[no_error_df['processState'] == '보호중', 'processState'] = 'C'  # 보호중
        no_error_df.loc[no_error_df['processState'] == '종료(입양)', 'processState'] = 'A'
        no_error_df.loc[no_error_df['processState'] == '종료(기증)', 'processState'] = 'A'
        no_error_df.loc[no_error_df['processState'] == '종료(자연사)', 'processState'] = 'D'
        no_error_df.loc[no_error_df['processState'] == '종료(안락사)', 'processState'] = 'D'
        no_error_df.loc[no_error_df['processState'] == '종료(반환)', 'processState'] = 'R'
        no_error_df.loc[no_error_df['processState'] == '종료(방사)', 'processState'] = 'E'
        no_error_df.loc[no_error_df['processState'] == '종료(미포획)', 'processState'] = 'E'
        no_error_df['processState_Pre'] = no_error_df['processState']
        no_error_df['processState']= no_error_df['processState_og']

        no_error_df['processState_C'] = no_error_df['processState'] == 'C'  # 보호중
        no_error_df['processState_A'] = no_error_df['processState'] == 'A'  # 입양+기증
        no_error_df['processState_D'] = no_error_df['processState'] == 'D'  # 자연사+안락사
        no_error_df['processState_R'] = no_error_df['processState'] == 'R'  # 반환
        no_error_df['processState_E'] = no_error_df['processState'] == 'E'  # 미포획+방사


        ### -process state_pre: 문자->숫자 mapping

        proc_mapping = {"C": 0, "A": 1, "D": 2, "R": 3, "E": 4}
        no_error_df['processState_Pre'] = no_error_df['processState_Pre'].map(proc_mapping)

        ### 성별( M=남, F=여자, Q=미상)
        no_error_df['sexCd_M'] = no_error_df['sexCd'] == 'M'
        no_error_df['sexCd_F'] = no_error_df['sexCd'] == 'F'
        no_error_df['sexCd_Q'] = no_error_df['sexCd'] == 'Q'
        no_error_df[['sexCd', 'sexCd_M', 'sexCd_F', 'sexCd_Q']].head(30)

        ### -neuterYn 문자-> 숫자
        sex_mapping = {"M": 0, "F": 1, "Q": 2}
        no_error_df['sexCd'] = no_error_df['sexCd'].map(sex_mapping)
        no_error_df.sexCd

        ### 중성화여부 (Y=중성화, N=중성화X, U=미확인)
        no_error_df['neuterYn_Y'] = no_error_df['neuterYn'] == 'Y'
        no_error_df['neuterYn_N'] = no_error_df['neuterYn'] == 'N'
        no_error_df['neuterYn_U'] = no_error_df['neuterYn'] == 'U'
        no_error_df[['neuterYn', 'neuterYn_Y', 'neuterYn_N', 'neuterYn_U']].head(20)

        ### neuterYn: 문자-> 숫자

        neuter_mapping = {"Y": 0, "N": 1, "U": 2}
        no_error_df['neuterYn'] = no_error_df['neuterYn'].map(neuter_mapping)
        no_error_df.neuterYn[1:3]

        ### 보호장소
        dfh1 = no_error_df['careNm'].str.contains('병원|의료센터|메디컬|클리닉|의료원')  # 메디컬(715)+의료(91)+의료(23408)
        dfh2 = no_error_df['careNm'].str.contains('보호소|보호센터|리본센터')  # 보호소(18387)+센터(18413)
        dfh3 = no_error_df['careNm'].str.contains('군청|시청')  # 군청(54)+시청(24)
        dfh4 = no_error_df['careNm'].str.contains('수의사회')  # 수의사회(2443)
        dfh5 = no_error_df['careNm'].str.contains('한동보|협회|보호협')  # 한동보(1115)+동물협회(10806)
        dfh6 = no_error_df['careNm'].str.contains('병원|의료|메디컬|클리닉|보호소|보호센터|리본센터|군청|시청|수의사회|한동보|협회|보호협|의료원') == False

        no_error_df['careNm_ETC'] = dfh6  # 밑에 컬럼속성들을 제외한 속성
        no_error_df['careNm_H'] = dfh1  # 병원,의료센터,메디컬,클리닉,의료원
        no_error_df['careNm_C'] = dfh2  # 보호소,보호센터,리본센터
        no_error_df['careNm_O'] = dfh3  # 군청, 시청
        no_error_df['careNm_AD'] = dfh4  # 수의사회
        no_error_df['careNm_CM'] = dfh5  # 한동보,동물협회

        ### Kind Cd

        no_error_df['kind'] = no_error_df['kindCd'].str.extract('([가-힣]+)\]', expand=False)  # 한글 정규식
        no_error_df['kind'].head()

        kind_mapping = {'개': 0, '고양이': 1, '기타축종': 2}
        no_error_df['kind'] = no_error_df['kind'].map(kind_mapping)
        no_error_df['breed'] = no_error_df['kindCd'].str.split('] ').str[1]

        #happenDt deep 카피
        no_error_df['og_happenDt'] = no_error_df['happenDt'].copy(deep=True)

        # 8자리를 날짜형식으로 바꿈
        print(no_error_df)
        no_error_df['happenDt'] = pd.to_datetime(no_error_df['happenDt'], format='%Y%m%d')


        # df['happenWd'] = df['happenDt'].dt.dayofweekday  # 요일을 숫자로 표현함 "0 = Sunday"
        no_error_df['happenWd'] = no_error_df['happenDt'].dt.day_name()

        # 날짜에서 '월'값을 받음
        no_error_df['happenMth'] = pd.DatetimeIndex(no_error_df['happenDt']).month

        # 시간형식으로 변경된 happenDt컬럼 드랍
        no_error_df = no_error_df.drop('happenDt', 1)


        ### - happenWd(발견요일) : 문자 -> 숫자 mapping
        week_mapping = {"Monday": 0, "Tuesday": 2, "Wednesday": 3,
                        "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
        no_error_df['happenWd'] = no_error_df['happenWd'].map(week_mapping)



        ### orgNm(담당지역주소): 두분류로 나눈뒤, 숫자 mapping
        no_error_df['sido'] = no_error_df['orgNm'].str.split(" ").str[0]
        sido_mapping = {"경기도": 0, "서울특별시": 1, "부산광역시": 2, "경상남도": 3,
                        "인천광역시": 4, "충청남도": 5, "강원도": 6, "대구광역시": 7,
                        "전라북도": 8, "경상북도": 9, "대전광역시": 10, "울산광역시": 11,
                        "충청북도": 12, "전라남도": 13, "제주특별자치도": 14, "광주광역시": 15,
                        "세종특별자치시": 16
                        }
        no_error_df['sido'] = no_error_df['sido'].map(sido_mapping)
        no_error_df['sido'].head(3)
        ### weight

        no_error_df['weight(after)'] = no_error_df['weight'].copy(deep=True)
        list_weight = []
        weights = no_error_df["weight(after)"]
        for i in weights:
            parse = re.sub('\(Kg\)', '', i)
            list_weight.append(float(parse))

        no_error_df['weight(after)'] = list_weight

        no_error_df.loc[no_error_df['weight(after)'] <= 3, 'size'] = '초소형'
        no_error_df.loc[(no_error_df['weight(after)'] > 3) & (no_error_df['weight(after)'] <= 9), 'size'] = '소형'
        no_error_df.loc[(no_error_df['weight(after)'] > 9) & (no_error_df['weight(after)'] <= 25), 'size'] = '중형'
        no_error_df.loc[no_error_df['weight(after)'] > 25, 'size'] = '대형'

        ### - size : 문자 -> 숫자 mapping
        no_error_df['size'].fillna('중형', inplace=True)
        size_mapping = {"대형": 0, "소형": 1, "중형": 2, "초소형": 3}
        no_error_df['size'] = no_error_df['size'].map(size_mapping)

        ### age
        no_error_df.loc[no_error_df['age(after)'] <= 1, 'age_u'] = '유견기'
        no_error_df.loc[(no_error_df['age(after)'] > 1) & (no_error_df['age(after)'] <= 9), 'age_u'] = '성견기'
        no_error_df.loc[no_error_df['age(after)'] > 9, 'age_u'] = '노견기'


        ### -age mapping
        age_mapping = {"노견기": 0, "성견기": 1, "유견기": 2}
        no_error_df['age_u'] = no_error_df['age_u'].map(age_mapping)

        #no_error_df = no_error_df.drop(['Unnamed: 0.1', 'Unnamed: 0.1.1', 'age(before)', 'weight(before)', 'breed'], axis=1)
        no_error_df.rename(columns={'age(after)': 'age_Pre'}, inplace=True)
        no_error_df.rename(columns={'weight(after)': 'weight_Pre'}, inplace=True)


        #df = df.drop(['Unnamed: 0.1', 'Unnamed: 0.1.1', 'age(before)', 'weight(before)', 'breed'], axis=1)
        no_error_df.rename(columns={'age(after)': 'age_Pre'}, inplace=True)
        no_error_df.rename(columns={'weight(after)': 'weight_Pre'}, inplace=True)
        no_error_df.rename(columns={'breed.1': 'breed_Pre'}, inplace=True)

        #크롤링형식으로 받아졌던 happenDt를 카피한 happenDt_og를 happenDt로 이름변경
        no_error_df.rename(columns={'og_happenDt': 'happenDt'}, inplace=True)

        columns = ['age_Pre', 'careAddr', 'careNm', 'careTel', 'chargeNm', 'colorCd', 'desertionNo', 'filename',
                   'happenDt', 'happenPlace','kindCd', 'neuterYn', 'noticeComment', 'noticeEdt', 'noticeNo', 'noticeSdt',
                   'officetel', 'orgNm','popfile', 'processState', 'sexCd', 'specialMark', 'weight_Pre', 'kind', 'breed_Pre',
                   'happenWd', 'happenMth', 'size', 'age_u','processState_Pre', 'processState_C', 'processState_A',
                   'processState_D', 'processState_R', 'processState_E', 'sexCd_M', 'sexCd_F', 'sexCd_Q', 'neuterYn_Y',
                   'neuterYn_N', 'neuterYn_U','careNm_ETC', 'careNm_H', 'careNm_C', 'careNm_O', 'careNm_AD', 'careNm_CM', 'sido']

        no_error_df = pd.DataFrame(no_error_df, columns=columns)

        print(no_error_df)

        no_error_df.to_csv('lostAnimal_20180907_20181108_preprocessing.csv', encoding='euc-kr')

        no_error_df.to_sql(name='animal_asdfasdf', con=engine, if_exists='append', index=False )

    conn.close()

    del list_temp[:]
    del list_temp2[:]
    print(list_temp2)

if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)

if __name__ == '__main__':
    #animal_crawling()
    db_save()