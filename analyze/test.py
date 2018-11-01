
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('final.csv',encoding='euc-kr')

print(df)
print(df.shape)
print(df.columns)

num = df.as_matrix()

print(num)
print(type(num))

#print(np.count_nonzero(num == True))
#print(np.count_nonzero(num == False))

print(datetime.today())
print(datetime.today().strftime(("%Y%m%d")))