
## mysql database에 있는 테이블 불러오기 (select)

import pymysql
import pandas as pd
import numpy as np


print("mysql 연결 시작---------------")
#mysql Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='qwer1234!', db='animaldb', charset='utf8')

# Connection으로부터 Dictionary cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

#SQL문 실행
sql = "select * from animal_new"
curs.execute(sql)

#데이터 Fetch

cols = ['kind', 'happenWd', 'happenMth', 'size', 'age_u', 'sexCd_M', 'sexCd_F',
       'sexCd_Q', 'neuterYn_Y', 'neuterYn_N', 'neuterYn_U', 'careNm_ETC',
       'careNm_H', 'careNm_C', 'careNm_O', 'careNm_AD', 'careNm_CM', 'sido',
       'processState_A', 'sido.1']

lst = []

rows = curs.fetchall()
for row in rows:
    #print(row)

    lst.append([row['kind'], row['happenWd'], row['happenMth'], row['size'], row['age_u'], row['sexCd_M'], row['sexCd_F'],
                row['sexCd_Q'], row['neuterYn_Y'], row['neuterYn_N'], row['neuterYn_U'], row['careNm_ETC'],
                row['careNm_H'], row['careNm_C'], row['careNm_O'], row['careNm_AD'], row['careNm_CM'], row['sido'],
                row['processState_A'], row['sido.1']])

conn.close()

df = pd.DataFrame(lst, columns=cols)
print("전일자 df 생성 완료-----------------")



from analyze.reference import prediction


P = np.array(df.drop(columns='processState_A'))
print(P)
print(P.shape)

if __name__ == '__main__':
    suc = prediction(P)
    print("함수 성공")
    print(suc)
    print(len(suc))

print(type(suc)) # numpy.ndarray

df2 = pd.DataFrame(suc)
df2.to_csv("final.csv", encoding='euc-kr', index=False)

#print(df.columns)
#print(len(df))
#print(df)




