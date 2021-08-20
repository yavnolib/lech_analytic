import pandas as pd
import datetime
pand = pd.read_excel('s.xlsx')
pand=pand[6:]
pand=pand.fillna(value=0)
balls=[]
for row in range(6,1218):
  if pand['Unnamed: 5'][row]=='общий конкурс':
     balls.append([pand['Unnamed: 3'][row],pand['Unnamed: 1'][row]])
import numpy as np
x=np.array(balls)
x=x[x[:,0].astype(int).argsort()]
dataset = pd.DataFrame({'Балл': x[::-1, 0], 'Чел': x[::-1, 1]})
dataset.to_excel('mark.xlsx',)
# mark.xlsx - итоговый файл с рейтинговой таблицей
