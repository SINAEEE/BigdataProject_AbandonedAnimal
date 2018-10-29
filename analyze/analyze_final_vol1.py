
## mysql database에 있는 테이블 불러오기 (select)

import pymysql
import pandas as pd
from .reference import test

##example 01

#mysql Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='animaldb', charset='utf8')

# Connection으로부터 Dictionary cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

#SQL문 실행
sql = "select * from animal_new"
curs.execute(sql)

#데이터 Fetch

cols = ['age(after)', 'age_u', 'careNm_AD', 'careNm_C', 'careNm_CM',
       'careNm_ETC', 'careNm_H', 'careNm_O', 'happenMth', 'happenWd', 'kind',
       'neuterYn', 'neuterYn_N', 'neuterYn_U', 'neuterYn_Y', 'noticeEdt',
       'orgNm', 'processState_A', 'processState_C', 'processState_D',
       'processState_E', 'processState_Pre', 'processState_R', 'sexCd',
       'sexCd_F', 'sexCd_M', 'sexCd_Q', 'size', 'weight(after)', 'sido']

lst = []

rows = curs.fetchall()
for row in rows:
    #print(row)

    lst.append([row['age(after)'], row['age_u'], row['careNm_AD'], row['careNm_C'], row['careNm_CM'],
          row['careNm_ETC'], row['careNm_H'], row['careNm_O'], row['happenMth'], row['happenWd'], row['kind'],
          row['neuterYn'], row['neuterYn_N'], row['neuterYn_U'], row['neuterYn_Y'], row['noticeEdt'],
          row['orgNm'], row['processState_A'], row['processState_C'], row['processState_D'],
          row['processState_E'], row['processState_Pre'], row['processState_R'], row['sexCd'],
          row['sexCd_F'], row['sexCd_M'], row['sexCd_Q'], row['size'], row['weight(after)'], row['sido']])

conn.close()

df = pd.DataFrame(lst, columns=cols)

#print(df.columns)
#print(len(df))
#print(df)




