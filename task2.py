# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:15:36 2018

@author: yipin
"""

import os
import pandas as pd
import re
import numpy as np
##Note: changing the directory is very important, otherwise there might be 
##some problems in importing the tabula package
project_root = 'D:/Research Assistant/task2/'
os.chdir(project_root)
import tabula

from tabula import read_pdf

##set the input of pages
n_pages = 131
year = 2011
import pandas as pd
##create the empty dataframe
df = pd.DataFrame(columns=['EJERCICIO LEGISLATIVO','DNI / CI',
                  'A. PATERNO','A. MATERNO','NOMBRES',
                  'AL INICIO', 'ENTREGA PERIÓDICA','AL CESAR',
                  'INGRESOS MENSUALES_SECTOR PÚBLICO',
                  'INGRESOS MENSUALES_SECTOR PRIVADO',
                  'INGRESOS MENSUALES_TOTAL S/.',
                  'OTROS *_SECTOR PÚBLICO',
                  'OTROS *_SECTOR PRIVADO',
                  'OTROS *_TOTAL S/.',
                  'BIENES **_SECTOR PÚBLICO',
                  'BIENES **_SECTOR PRIVADO',
                  'BIENES **_TOTAL S/.',
                  'OTRA INFORMACIÓN QUE CONSIDERE EL OBLIGADO',
                  'OTRA INFORMACIÓN_TOTAL S/.'])

## read data
for i in range(1, n_pages+1,1):
    
    df_temp = tabula.read_pdf(str(year)+".pdf", pages=i, multiple_tables=True, 
                              encoding = 'ISO8859_1' )
    

    time = df_temp[0]
    name = df_temp[1]
    period = df_temp[2]
    income = df_temp[3]
    other_info = df_temp[4]
    
    df.loc[i, 'EJERCICIO LEGISLATIVO'] = time.iloc[2,1]
    #name
    df.loc[i, 'DNI / CI'] =  name.iloc[0,1]
    df.loc[i, 'A. PATERNO'] = name.iloc[1,1]
    df.loc[i, 'A. MATERNO'] = name.iloc[2,1]
    df.loc[i, 'NOMBRES'] = name.iloc[3,1]
    #period
    df.loc[i,'AL INICIO'] = period.iloc[0,1]
    df.loc[i,'ENTREGA PERIÓDICA'] = period.iloc[1,1]
    df.loc[i,'AL CESAR'] = period.iloc[2,1]

    df.loc[i,'INGRESOS MENSUALES_SECTOR PÚBLICO'] = income.iloc[1,1]
    df.loc[i,'INGRESOS MENSUALES_SECTOR PRIVADO'] = income.iloc[1,2]
    df.loc[i,'INGRESOS MENSUALES_TOTAL S/.'] = income.iloc[1,3]
    df.loc[i,'OTROS *_SECTOR PÚBLICO'] = income.iloc[2,1]
    df.loc[i,'OTROS *_SECTOR PRIVADO'] = income.iloc[2,2]
    df.loc[i,'OTROS *_TOTAL S/.'] = income.iloc[2,3]
    df.loc[i,'BIENES **_SECTOR PÚBLICO'] = income.iloc[3,1]
    df.loc[i,'BIENES **_SECTOR PRIVADO'] = income.iloc[3,2]
    df.loc[i,'BIENES **_TOTAL S/.'] = income.iloc[3,3]

    ##read the other information.
    ## Because the tabula might give different columns for other information.
    ## I use the codes below to extract other information
    ## the break mark is "---"
    if (other_info.shape[0] > 1):
        other_info1 = ''
        other_info2 =''
        for m in range(1,len(other_info)):
            for j in range(0, other_info.shape[1]-1):
                if (str(other_info.iloc[m,j]) != 'nan'):
                    other_info1 += other_info.iloc[m,j]+'---'
            if (str(other_info.iloc[m,other_info.shape[1]-1])!= 'nan'):
                other_info2 += other_info.iloc[m,other_info.shape[1]-1] + '---'
        df.loc[i,'OTRA INFORMACIÓN QUE CONSIDERE EL OBLIGADO'] = other_info1
        df.loc[i,'OTRA INFORMACIÓN_TOTAL S/.'] = other_info2





"""
Some columns might be empty, therefore I use additional codes to deal with errors
 #else:
        #df.loc[i,'OTRA INFORMACIÓN QUE CONSIDERE EL OBLIGADO'] = float(nan)
        #df.loc[i,'OTRA INFORMACIÓN_TOTAL S/.'] = float(nan)
    #for 2011, page 71
    df.loc[i,'INGRESOS MENSUALES_SECTOR PÚBLICO'] = income.iloc[1,1]
    df.loc[i,'INGRESOS MENSUALES_SECTOR PRIVADO'] = income.iloc[1,2]
    df.loc[i,'INGRESOS MENSUALES_TOTAL S/.'] = income.iloc[1,3]
    df.loc[i,'OTROS *_SECTOR PÚBLICO'] = np.nan
    df.loc[i,'OTROS *_SECTOR PRIVADO'] = np.nan
    df.loc[i,'OTROS *_TOTAL S/.'] = np.nan
    df.loc[i,'BIENES **_SECTOR PÚBLICO'] = income.iloc[2,1]
    df.loc[i,'BIENES **_SECTOR PRIVADO'] = income.iloc[2,2]
    df.loc[i,'BIENES **_TOTAL S/.'] = income.iloc[2,3]


"""

###--clean data. Some numbers contains "'" or "?"
    df['INGRESOS MENSUALES_SECTOR PÚBLICO'] = df['INGRESOS MENSUALES_SECTOR PÚBLICO'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['INGRESOS MENSUALES_SECTOR PRIVADO'] = df['INGRESOS MENSUALES_SECTOR PRIVADO'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['INGRESOS MENSUALES_TOTAL S/.'] = df['INGRESOS MENSUALES_TOTAL S/.'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['OTROS *_SECTOR PÚBLICO'] = df['OTROS *_SECTOR PÚBLICO'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['OTROS *_SECTOR PRIVADO'] = df['OTROS *_SECTOR PRIVADO'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['OTROS *_TOTAL S/.'] = df['OTROS *_TOTAL S/.'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['BIENES **_SECTOR PÚBLICO'] = df['BIENES **_SECTOR PÚBLICO'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['BIENES **_SECTOR PRIVADO'] = df['BIENES **_SECTOR PRIVADO'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    df['BIENES **_TOTAL S/.'] = df['BIENES **_TOTAL S/.'].str.replace('?', ',').str.replace("'", ',').str.replace(" ","")
    #df['OTRA INFORMACIÓN QUE CONSIDERE EL OBLIGADO'] = df['OTRA INFORMACIÓN QUE CONSIDERE EL OBLIGADO'].replace('?', '')
    df['OTRA INFORMACIÓN_TOTAL S/.'] = df['OTRA INFORMACIÓN_TOTAL S/.'].str.replace('?', ',')
    df['DNI / CI'] = df['DNI / CI'].astype(str)

## for those whose first number is 0
for i in range(1,n_pages+1):
    if df.loc[i,'DNI / CI'][0] == '0':
        df.loc[i,'DNI / CI'] = "'"+df.loc[i,'DNI / CI']


df.to_csv('D:/Research Assistant/Task2/'+str(year)+'.csv', encoding = 'utf-8-sig', index = False)  
    