import pandas as pd #Importing the library for working with data structures (clearing it, chek it, manipulate)
import numpy as np #Importing the library for manipulating arrays, matrices and maths
from Resumen import ResumenDf #Importing the 'Resumen' module which automates an important part of the cleaning process, allowing to decide faster

pd.set_option('display.max_columns', 22) #Set the max number of columns/rows to be displayed 
pd.set_option('display.max_rows', 50)

raw21 = pd.read_excel(r"datos clima\BD_2021.xlsx") #Read the path where the excel is located
ResumenDf(raw21)

#UVI, NO, NOX are columns full of NaN values ... 90-100% NaN = 100% Sure those must be droped
raw21.drop(["UVI","NO","NOX"], axis=1, inplace=True) #raw18=raw19.drop(......, inplace= False) is equivalent to this line of code

ResumenDf(raw21) 

raw21.dropna(subset=['PM2.5'], inplace=True) #Drop any row with our target variable missing
ResumenDf(raw21)

#Those 6 presented a missing percentage over 30% so get droped
raw21.drop(["NO2","RS",], axis=1, inplace=True) #raw18=raw19.drop(......, inplace= False) is equivalent to this line of code
ResumenDf(raw21)

print(raw21["PP"].describe())#To see how often I recieve a value diferent from zero, this means how often rains, showed 75%--->0, It doesn't rain most of the time 
raw21['PP'] = raw21['PP'].fillna(0) #Based on that 75% I prefered fill NaN values with 0 instead with mean, using the mean i´ts like "creating" a mini rain when it´s probably never rained
cl21 = raw21.fillna(raw21.mean(numeric_only=True)) #The rest of the columns with a missing data percentage under 20% decided to input using the mean of it´s column
ResumenDf(cl21)

cl21.to_excel("Clear21.xlsx", index=False) #Downloaded the clean dataframe
