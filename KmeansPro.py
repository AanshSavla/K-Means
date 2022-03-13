# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:51:07 2020

@author: User
"""

import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt

center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])

data_1 = np.random.randn(200,2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3

data=np.concatenate((data_1,data_2,data_3),axis=0)

plt.scatter(data[:,0],data[:,1],s=7)

k=3
n=data.shape[0]#row
c=data.shape[1]#column

mean = np.mean(data,axis=0)
std = np.mean(data,axis=0)
centers = np.random.randn(k,c)*std + mean

plt.scatter(data[:,0],data[:,1],s=7)
plt.scatter(centers[:,0],centers[:,1],marker='*',c='g',s=150)
