#This script is to see which variables we´re gonna use for our model

import pandas as pd #Importing the library for working with data structures (clearing it, chek it, manipulate)
import numpy as np #Importing the library for manipulating arrays, matrices and maths

pd.set_option('display.max_columns', 22) #Set the max number of columns/rows to be displayed 
pd.set_option('display.max_rows', 50)

cl18 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\Cleared_Data\Clear18.xlsx") #Read the path where the excel is located
cl19 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\Cleared_Data\Clear19.xlsx") #Read the path where the excel is located
cl20 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\Cleared_Data\Clear20.xlsx") #Read the path where the excel is located
cl21 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\Cleared_Data\Clear21.xlsx") #Read the path where the excel is located
cl22 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\Cleared_Data\Clear22.xlsx") #Read the path where the excel is located
cl23 = pd.read_excel(r"Kaggle_CosasSerias_DataScience\Datos\PM2.5_SEMADET\Cleared_Data\Clear23.xlsx") #Read the path where the excel is located

#Build a dictionary for our columns
Dict_Comp = {
    "L18" : cl18.columns,
    "L19" : cl19.columns,
    "L20" : cl20.columns,
    "L21" : cl21.columns,
    "L22" : cl22.columns,
    "L23" : cl23.columns,
}

data = [] #Hollow list

for year, val in Dict_Comp.items():#This shows key-value
    print(f"{year},{val}\n")
    for i in val:#Our value is a list, so we use another 'for' 
        print(i)
        data.append([year,i])#Append each year with every single value in the list

print(data)

Comp = pd.DataFrame(data, columns=['AÑO','Variable']) #Build a df just to check
print(Comp.head)

print(Comp["Variable"].value_counts())#Shows the frequency of each unique value

#Based on that those with a frequency less than 4 must be droped, the remainig variables are going to be considered by EDA