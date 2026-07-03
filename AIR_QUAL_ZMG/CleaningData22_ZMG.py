import pandas as pd #Importing the library for working with data structures (clearing it, chek it, manipulate)
import numpy as np #Importing the library for manipulating arrays, matrices and maths
from Resumen import ResumenDf #Importing the 'Resumen' module which automates an important part of the cleaning process, allowing to decide faster

pd.set_option('display.max_columns', 22) #Set the max number of columns/rows to be displayed 
pd.set_option('display.max_rows', 50)

raw22 = pd.read_excel(r"datos clima\BD_2022.xlsx") #Read the path where the excel is located
ResumenDf(raw22)

#NO2, NOX, NO, UVI, are columns full of NaN values ... 90-100% NaN = 100% Sure those must be droped
raw22.drop(["NO2","NOX","NO","UVI"], axis=1, inplace=True) #raw22=raw22.drop(......, inplace= False) is equivalent to this line of code

ResumenDf(raw22)

raw22.dropna(subset=['PM2.5'], inplace=True) #Drop any row with our target variable missing
ResumenDf(raw22)

#Those 6 presented a missing percentage over 30% so get droped
raw22.drop(["SO2","WD","CO","RS","ET","PP","ATM","RH"], axis=1, inplace=True) #raw18=raw19.drop(......, inplace= False) is equivalent to this line of code
ResumenDf(raw22)

cl22 = raw22.fillna(raw22.mean(numeric_only=True)) #The rest of the columns with a missing data percentage under 20% decided to input using the mean of it´s column
ResumenDf(cl22)

cl22.to_excel("Clear22.xlsx", index=False) #Downloaded the clean dataframe
