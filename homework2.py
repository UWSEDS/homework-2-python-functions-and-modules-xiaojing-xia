#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


def read_url(url):
    data=pd.read_csv(url)
    return data


# In[ ]:


def test_create_dataframe(df,column_list):
    (row_count,column_count)=df.shape
    temp=1
    if row_count < 10:
        print("There are at least 10 rows in the DataFrame - False")
        return False
    else:
        print("There are at least 10 rows in the DataFrame - True")
        for i in range(0,column_count):
            if (df.columns[i] in column_list):
                temp=temp*1
            else:
                temp=0
        if temp==0:
            print("The DataFrame contains only the columns that you specified as the second argument - False")
            return False
        else:
            print("The DataFrame contains only the columns that you specified as the second argument - True")
            for m in range(0,column_count-1):
                if (df[df.columns[m]].dtypes)!=(df[df.columns[m+1]].dtypes):
                    temp=0
            if temp==0:
                print("The values in each column have the same python type - False")
                return False
            else:
                print("The values in each column have the same python type - True")
                return True
            
                

