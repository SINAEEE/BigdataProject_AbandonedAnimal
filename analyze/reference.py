
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn import metrics, preprocessing
from scipy.stats import itemfreq






### 데이터 불러오기

df5=pd.read_csv("./csv_dir/lostAnimal_20150101_20151231_vol3.csv", encoding="euc-kr")
df6=pd.read_csv("./csv_dir/lostAnimal_20160101_20161231_vol3.csv", encoding="euc-kr")
df7=pd.read_csv("./csv_dir/lostAnimal_20170101_20171231_vol3.csv", encoding="euc-kr")
df8=pd.read_csv("./csv_dir/lostAnimal_20180101_20181231_vol3.csv", encoding="euc-kr")

#print(df5.tail())

df5 = df5.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'])
df6 = df6.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'])
df7 = df7.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'])
df8 = df8.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'])

#print(len(df5.columns))
#print(len(df6.columns))
#print(len(df7.columns))
#print(len(df8.columns))



### 데이터프레임 합치기(15,16,17년도)

df567 = pd.concat([df5,df6], ignore_index=True)
df567 = pd.concat([df567,df7], ignore_index=True)
print("\n15,16,17년도 데이터프레임 총 행수 : {}".format(len(df567)))
print("18년도 데이터프레임 총 행수 : {}".format(len(df8)))

print("\n15,16,17년도 데이터프레임 column 명 : {}".format(df567.columns))
print("18년도 데이터프레임 column 명  : {}".format(df8.columns))


### 필요없는 컬럼 삭제

df = df567.drop(columns=['age(before)','colorCd','careAddr', 'careNm', 'careTel', 'chargeNm',
                      'desertionNo', 'filename', 'happenDt', 'happenPlace', 'kindCd','noticeComment',
                       'noticeNo', 'noticeSdt','officetel', 'popfile', 'processState',
                       'weight(before)', 'specialMark','breed', 'breed_Pre','breed.1'
                      ])

df_t = df8.drop(columns=['age(before)','colorCd','careAddr', 'careNm', 'careTel', 'chargeNm',
                      'desertionNo', 'filename', 'happenDt', 'happenPlace', 'kindCd','noticeComment',
                       'noticeNo', 'noticeSdt','officetel', 'popfile', 'processState',
                       'weight(before)', 'specialMark','breed', 'breed_Pre'
                      ])


print("\n15/16/17년도 데이터프레임 사용할 컬럼 갯수 : ",len(df.columns))
print("컬럼 이름 : ", df.columns)

print("18년도 데이터프레임 사용할 컬럼 갯수 : ",len(df_t.columns))
print("컬럼 이름 : ", df_t.columns)


### 결측치 처리

null_columns=df.columns[df.isnull().any()]
print("\n15/16/17년도 데이터프레임 결측치 : ")
print(df[null_columns].isnull().sum())

null_columns2=df_t.columns[df_t.isnull().any()]
print("18년도 데이터프레임 결측치 : ")
print(df_t[null_columns2].isnull().sum())


# weight(after) : 나이별로 묶어서 중위값넣기
df["weight(after)"].fillna(df.groupby("age_u")["weight(after)"].transform("median"), inplace=True)
df_t["weight(after)"].fillna(df_t.groupby("age_u")["weight(after)"].transform("median"), inplace=True)

print("\nweight(after)컬럼 결측치 재확인 : ")
print(df.loc[pd.isnull(df["weight(after)"])])
print(df_t.loc[pd.isnull(df["weight(after)"])])


# size : 몸무게가 비어서 전처리 되지 않은 행 재전처리
df.loc[df['weight(after)'] <= 3, 'size'] = '초소형'
df.loc[(df['weight(after)'] > 3 ) & (df['weight(after)'] <=9 ), 'size'] = '소형'
df.loc[(df['weight(after)'] > 9 ) & (df['weight(after)'] <=25 ), 'size'] = '중형'
df.loc[df['weight(after)'] > 25, 'size'] = '대형'

df_t.loc[df_t['weight(after)'] <= 3, 'size'] = '초소형'
df_t.loc[(df_t['weight(after)'] > 3 ) & (df_t['weight(after)'] <=9 ), 'size'] = '소형'
df_t.loc[(df_t['weight(after)'] > 9 ) & (df_t['weight(after)'] <=25 ), 'size'] = '중형'
df_t.loc[df_t['weight(after)'] > 25, 'size'] = '대형'

print("\nsize컬럼 결측치 재확인 : ")
print(df.loc[pd.isnull(df["size"])])
print(df_t.loc[pd.isnull(df_t["size"])])


### mapping

# neuterYn : 문자 -> 숫자
neuter_mapping = {"Y":0,"N":1,"U":2}
df['neuterYn'] = df['neuterYn'].map(neuter_mapping)
df_t['neuterYn'] = df_t['neuterYn'].map(neuter_mapping)

print("\n15,16,17년도 중성화여부 전처리 확인 : \n{}".format(df.neuterYn[1:3]))
print("18년도 중성화여부 전처리 확인 : \n{}".format(df_t.neuterYn[1:3]))


# sexCd : 문자 -> 숫자
sex_mapping = {"M":0,"F":1,"Q":2}
df['sexCd'] = df['sexCd'].map(sex_mapping)
df_t['sexCd'] = df_t['sexCd'].map(sex_mapping)

print("\n15,16,17년도 성별 전처리 확인 : \n{}".format(df.sexCd[1:3]))
print("18년도 성별 전처리 확인 : \n{}".format(df_t.sexCd[1:3]))


# orgNm(담당지역주소) : 두분류로 나눈뒤, 숫자 mapping
df['sido'] = df['orgNm'].str.split(" ").str[0]
df_t['sido'] = df_t['orgNm'].str.split(" ").str[0]

print("\n15,16,17년도 지역별 보호기관 수 \n{}".format(df['sido'].value_counts()))
print("\n18년도 지역별 보호기관 수 \n{}".format(df_t['sido'].value_counts()))

sido_mapping = {"경기도":0,"서울특별시":1,"부산광역시":2,"경상남도":3,
                "인천광역시":4,"충청남도":5,"강원도":6,"대구광역시":7,
                "전라북도":8,"경상북도":9,"대전광역시":10,"울산광역시":11,
                "충청북도":12,"전라남도":13,"제주특별자치도":14,"광주광역시":15,
                "세종특별자치시":16
}
df['sido'] = df['sido'].map(sido_mapping)
df_t['sido'] = df_t['sido'].map(sido_mapping)

print("\n15,16,17년도 지역 전처리 확인 : \n{}".format(df['sido'].head(3)))
print("\n18년도 지역 전처리 확인 : \n{}".format(df_t['sido'].head(3)))


# happenWd(발견요일) : 문자-> 숫자 mapping
week_mapping = {"Monday":0, "Tuesday":2, "Wednesday":3,
                "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}
df['happenWd'] = df['happenWd'].map(week_mapping)
df_t['happenWd'] = df_t['happenWd'].map(week_mapping)

print("\n15,16,17년도 발견요일 전처리 확인 : \n{}".format(df['happenWd'].head(3)))
print("\n18년도 발견요일 전처리 확인 : \n{}".format(df_t['happenWd'].head(3)))


# size : 문자 -> 숫자 mapping
size_mapping = {"대형":0,"소형":1,"중형":2,"초소형":3}
df['size'] = df['size'].map(size_mapping)
df_t['size'] = df_t['size'].map(size_mapping)

print("\n15,16,17년도 size 전처리 확인 : \n{}".format(df['size'].head(3)))
print("\n18년도 size 전처리 확인 : \n{}".format(df_t['size'].head(3)))


# age : 문자 -> 숫자 mapping
age_mapping = {"노견기":0,"성견기":1,"유견기":2}
df['age_u'] = df['age_u'].map(age_mapping)
df_t['age_u'] = df_t['age_u'].map(age_mapping)

print("\n15,16,17년도 age 전처리 확인 : \n{}".format(df['size'].head(3)))
print("\n18년도 age 전처리 확인 : \n{}".format(df_t['size'].head(3)))


# processState_Pre : 문자 -> 숫자 mapping
proc_mapping = {"C":0, "A":1, "D":2, "R":3, "E":4}
df['processState_Pre'] = df['processState_Pre'].map(proc_mapping)
df_t['processState_Pre'] = df_t['processState_Pre'].map(proc_mapping)

print("\n15,16,17년도 현재상태 전처리 확인 : \n{}".format(df['processState_Pre'].head(3)))
print("\n18년도 현재상태 전처리 확인 : \n{}".format(df_t['processState_Pre'].head(3)))


### 사용할 feature 선택

feature_name = ['kind', 'happenWd', 'happenMth','size','age_u', 'sexCd_M',
               'sexCd_F', 'sexCd_Q', 'neuterYn_Y', 'neuterYn_N', 'neuterYn_U',
               'careNm_ETC', 'careNm_H', 'careNm_C', 'careNm_O', 'careNm_AD',
               'careNm_CM', 'sido','processState_A', 'sido']
df_A = df[feature_name]
dft_A = df_t[feature_name]


### 종속변수 독립변수 추출
X=np.array(df_A.drop(columns='processState_A')) #종속변수 train
Y=np.array(df_A.processState_A) #독립변수 train
X2=np.array(dft_A.drop(columns='processState_A')) #종속변수 test
Y2=np.array(dft_A.processState_A) #독립변수 test

print(X.shape)
print(Y.shape)
print(X2.shape)
print(Y2.shape)



### ---------------------------------------------------------모형적용

knn = KNeighborsClassifier(n_neighbors=1) # n_neighbor : 이웃의 갯수
print(knn)
knn.fit(X, Y)
print("\n------knn모델생성 완료------\n")


### 예측 및 검증
X_new = np.array([[0,3,11,2,1,0,0,1,1,0,0,0,0,0,1,0,0,4,3]])
print("X_new.shape : {}".format(X_new.shape))
target_A = {0:'입양X', 1:'입양O'}


# test 값에 대한 예측
Y_pred = knn.predict(X)
print("\n테스트 셋에 대한 예측값: {}".format(Y_pred))


# 임의의 생성값에 대한 예측
prediction_A = knn.predict(X_new)
print("\n임의의 생성값에 대한 예측:{}".format(prediction_A))
p_A = int(prediction_A)
print("\n 임의의 생성값으로 예측한 타깃의 이름 : {}".format(target_A[p_A]))


def prediction(p1):

   prediction_Y = knn.predict(p1)
   return prediction_Y



# 검증
print( "\nKNN best accuracy : " + str(np.round(metrics.accuracy_score(Y,Y_pred),3)))


