# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:02:15 2022

@author: PC
"""
def findMedian(arr):
    # Write your code here
    a=sorted(arr)
    b=int((len(arr)-1)/2)
    c=a[b]
    return c

#%%

f=[1,5,3,4,2,0,6]
a=sorted(f)
b=int((len(a)-1)/2)
c=a[b]
#%%

f=[1,1,2,2,2,3]

a=f.count(f[1])
