# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:49:11 2017

@author: vicio
"""

list1 = list([word.split(";")[:-1] for word in open("dati1.dat","r")])[:-1]
X=[]
Y=[]
Z=[]

for i in range(len(list1)):
    X.append(float(list1[i][0]))
    Y.append(float(list1[i][1]))
    Z.append(float(list1[i][2]))

X=[]
Y=[]
Z=[]
X = list(float(list1[i][0]) for i in range(len(list1)))
Y = list(float(list1[i][1]) for i in range(len(list1)))
Z = list(float(list1[i][2]) for i in range(len(list1)))

