#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv 
with open('frut.csv') as file_obj: 
   reader_obj = csv.reader(file_obj) 
   for row in reader_obj: 
        print(row)

