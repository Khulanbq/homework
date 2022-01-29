# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("khulan's first try")


 import pandas as pd
 import os
 
 pd.set_option('display.max_rows', 500)
 pd.set_option('display.max_columns', 500)
 pd.set_option('display.width', 1000)
 
os.getcwd()
os.chdir("2_Data_and_Control_Flow\\data")

df=pd.read_csv("data.csv")
df

# import data files
df_ind   = pd.read_excel('data_more.xlsx', sheet_name='loan_ind',
    usecols='D:I,L',skiprows=6, header=None)

df.head()
list(df.columns)
df.columns
df.values

df["salary_new"]=df["salary"]*1.1
df["growth"]=df["salary_new"]/df["salary"]

df.to_csv("datanew.csv")
del df["growth"]
df[['salary', 'age']]

df.columns=['cid', 'firstName', 'lastName', 'citizenId', 'abage', 'yearsInCompany', 'ssalary', 'gender', 'startDate', 'politicalView', 'salary_new']



 import numpy as np
 
np.eye(5) # unit matrix
np.eye(5,3)

# array and array operation
a = np.array([1, 2, 3, 4])
b = np.ones(4) + 1
a + 1
2**a  # powers of 2
a - b # difference 
j = np.arange(5)
2**(j + 1) - j # power of two and subtract


# reshape or broadcast
a = np.arange(9).reshape(3, 3)
a.T

A = np.arange(12).reshape(3,4)
b = np.repeat(A[:,:,np.newaxis], 2, axis=-1) # Using repeat to add a new dimension at the end
b = np.repeat(A[:,:,np.newaxis], 2, axis=1)
b = np.repeat(A[:,:,np.newaxis], 2, axis=0)
b = np.repeat(A[:,:,np.newaxis], 2, axis=2)

b = np.repeat(A[np.newaxis,:,:], 2, axis=0)
b = np.repeat(A[:,np.newaxis,:], 2, axis=0)

A[:,np.newaxis,:][:,1,:]
b[:,0,:]
b = np.repeat(A[:,:,np.newaxis], 2, axis=0)
b[:,:,0]

b = np.repeat(A[:,:,np.newaxis], 2, axis=1)
b[:,:,0]

b = np.repeat(A[:,:,np.newaxis], 2, axis=2)
b[:,:,0]
b[:,:,1]

b = np.repeat(A[:,np.newaxis,:], 2, axis=1)
b[:,1,:]

b = np.repeat(A[:,np.newaxis,:], 2, axis=0)
b[:,1,:]
b[0,:,:]
b[:,0,:]

np.tile(A, (2,1,1))  # add a new dimension at the beginning
np.repeat(A[None,:,:], 2, axis=0) # add a new dimension at the beginning
np.tile(A, (1,1,2))

# ravel and flatten
a = np.array([[1, 2, 3], [4, 5, 6]])
a.flatten()
a.ravel()

# linspace
b = np.linspace(0.0, 10.0, num=100)
np.sin(b)

b = np.linspace(0.0, 10.0, num=10)
b = np.linspace(0.0, 10.0, num=11)
np.linspace(4.0, 6.0, num=3)



 import pandas as pd
 import os
 
 pd.set_option('display.max_rows', 500)
 pd.set_option('display.max_columns', 500)
 pd.set_option('display.width', 1000)
 
os.getcwd()

df=pd.read_csv("data.csv")
df
type(df.values)
numdf=df.values
numdf.repeat(2,axis=0)