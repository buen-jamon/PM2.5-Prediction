import pandas as pd #Importing the library for working with data structures (clearing it, chek it, manipulate)
import numpy as np #Importing the library for manipulating arrays, matrices and maths

pd.set_option('display.max_columns', 22) #Set the max number of columns/rows to be displayed 
pd.set_option('display.max_rows', 50)

raw18 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\BD_2018.xlsx") #Read the path where the excel is located
print(raw18.head()) #Shows the first five rows of our dataframe
print(raw18.dtypes) #Print the type of data of each column

print((raw18.isna().mean()*100).sort_values(ascending=False)) #.isna retrieves a array where if theres a NaN the value is filled with 'True' otherwise is 'False' both are equivalent to 0 n' 1 
#so with .mean() it adds each element and divides by the number of values * 100 transforms into percentage and .sort_values(ascending=False) ordenates max-min or min-max if we set it as 'True'

#UVI, NO, NOX are columns full of NaN values ... 100% NaN = 100% Sure those must be droped
print(raw18[['UVI']].isna())
raw18.drop(["UVI","NO","NOX","RS","ET","ATM","RH"], axis=1, inplace=True) #raw18=raw18.drop(......, inplace= False) is equivalent to this line of code
print(raw18.head()) #Dataframe succesfully changed (Those 3)

raw18.dropna(subset=['PM2.5'], inplace=True)
print(raw18.head())
print((raw18.isna().mean()*100).sort_values(ascending=False))


raw18['PP'] = raw18['PP'].fillna(0)
cl18 = raw18.fillna(raw18.mean(numeric_only=True))
print(cl18.head())
print((cl18.isna().mean()*100).sort_values(ascending=False))

print(cl18["PP"].describe())

cl18.to_excel("Clear18.xlsx", index=False)
