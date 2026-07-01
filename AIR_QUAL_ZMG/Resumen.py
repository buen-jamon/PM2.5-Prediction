import pandas as pd #Importing the library for working with data structures (clearing it, chek it, manipulate)
import numpy as np #Importing the library for manipulating arrays, matrices and maths

pd.set_option('display.max_columns', 22) #Set the max number of columns/rows to be displayed 
pd.set_option('display.max_rows', 50)

#Created a function to automate some parts of our cleaning process
def ResumenDf(DataFrame):
    print(DataFrame.head()) #Shows the first five rows of our dataframe
    print(DataFrame.dtypes) #Print the type of data of each column
    print((DataFrame.isna().mean()*100).sort_values(ascending=False)) #.isna retrieves a array where if theres a NaN the value is filled with 'True' otherwise is 'False' both are equivalent to 0 n' 1 
    #so with .mean() it adds each element and divides by the number of values * 100 transforms into percentage and .sort_values(ascending=False) ordenates max-min or min-max if we set it as 'True'
