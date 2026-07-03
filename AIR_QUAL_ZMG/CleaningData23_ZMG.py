import pandas as pd #Importing the library for working with data structures (clearing it, chek it, manipulate)
import numpy as np #Importing the library for manipulating arrays, matrices and maths
from Resumen import ResumenDf #Importing the 'Resumen' module which automates an important part of the cleaning process, allowing to decide faster

pd.set_option('display.max_columns', 22) #Set the max number of columns/rows to be displayed 
pd.set_option('display.max_rows', 50)

raw23 = pd.read_excel(r"datos clima\BD_2023.xlsx") #Read the path where the excel is located
ResumenDf(raw23)

#NO2, NO, NOX, UVI, RS, are columns full of NaN values ... 90-100% NaN = 100% Sure those must be droped
raw23.drop(["NO2","NO","NOX","UVI","RS"], axis=1, inplace=True) #raw22=raw22.drop(......, inplace= False) is equivalent to this line of code

ResumenDf(raw23)

raw23.dropna(subset=['PM2.5'], inplace=True) #Drop any row with our target variable missing
ResumenDf(raw23)

#Those 6 presented a missing percentage over 30% so get droped
raw23.drop(["CO","ATM","SO2","PP","WD"], axis=1, inplace=True) #raw18=raw19.drop(......, inplace= False) is equivalent to this line of code
ResumenDf(raw23)

cl23 = raw23.fillna(raw23.mean(numeric_only=True)) #The rest of the columns with a missing data percentage under 20% decided to input using the mean of it´s column
ResumenDf(cl23)

cl23.to_excel("Clear23.xlsx", index=False) #Downloaded the clean dataframe















