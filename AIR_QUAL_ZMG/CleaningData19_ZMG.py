import pandas as pd #Importing the library for working with data structures (clearing it, chek it, manipulate)
import numpy as np #Importing the library for manipulating arrays, matrices and maths
from Resumen import ResumenDf #Importing the 'Resumen' module which automates an important part of the cleaning process, allowing to decide faster

pd.set_option('display.max_columns', 22) #Set the max number of columns/rows to be displayed 
pd.set_option('display.max_rows', 50)

raw19 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\BD_2019.xlsx") #Read the path where the excel is located
ResumenDf(raw19)

#UVI, NO, NOX are columns full of NaN values ... 100% NaN = 100% Sure those must be droped
raw19.drop(["UVI","NO","NOX"], axis=1, inplace=True) #raw18=raw19.drop(......, inplace= False) is equivalent to this line of code
ResumenDf(raw19)
raw19.dropna(subset=['PM2.5'], inplace=True) #Drop any row with our target variable missing
ResumenDf(raw19)
#Those 4 presented a missing percentage over 40% so get droped
raw19.drop(["ET","O3","RS","PP"], axis=1, inplace=True) #raw18=raw19.drop(......, inplace= False) is equivalent to this line of code
ResumenDf(raw19)
cl19 = raw19.fillna(raw19.mean(numeric_only=True)) #The rest of the columns with a missing data percentage under 20% decided to input using the mean of it´s column
ResumenDf(cl19)
cl19.to_excel("Clear19.xlsx", index=False) #Downloaded the clean dataframe
