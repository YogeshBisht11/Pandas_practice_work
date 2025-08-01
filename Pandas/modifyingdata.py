# -*- coding: utf-8 -*-
"""ModifyingData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hNglEBs9r_mYqeXS7MC6gDCLUZiZLX-Y

Adding a new column
"""

import pandas as pd
data={
    "name":['ram','shyam','ghanshyam','dhanshyam','aditi','jagdish','raj','simran'],
    "age":[22,25,33,28,33,35,30,23],
    "salary":[50000,40000,35000,56000,25000,38000,45000,57000],
    "performance score":[85,90,78,92,88,95,80,89]

}
df=pd.DataFrame(data)
print(df)

#direct method df["column_name"]=values
df["bonus"]=df['salary']*0.1
print(df)

#using insert()
#syntax:df.insert(loc,"column_name",some_data)
df.insert(0,"employee__id",[10,20,30,40,50,60,70,80])
print(df)

"""2.updating values"""

import pandas as pd
data={
    "name":['ram','shyam','ghanshyam','dhanshyam','aditi','jagdish','raj','simran'],
    "age":[22,25,33,28,33,35,30,23],
    "salary":[50000,40000,35000,56000,25000,38000,45000,57000],
    "performance score":[85,90,78,92,88,95,80,89]

}
df=pd.DataFrame(data)
print(df)

#to update a specific value - loc[] method
#syntax:df.loc[row_index,"column_name"]=new_vallue
df.loc[0,'salary']=55000
print(df)

#updating multiple values
#increasing salary by 5%
df['salary']=df['salary']*0.5
print(df)

"""removing data: using DROP() METHOD"""

import pandas as pd
data={
    "name":['ram','shyam','ghanshyam','dhanshyam','aditi','jagdish','raj','simran'],
    "age":[22,25,33,28,33,35,30,23],
    "salary":[50000,40000,35000,56000,25000,38000,45000,57000],
    "performance score":[85,90,78,92,88,95,80,89]

}
df=pd.DataFrame(data)
print(df)

#Syantx:df.drop(columns=["columnname"],inplace=true)
print('modified data')
df.drop(columns=["performance_score"],inplace=True)
print(df)