# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:36:50 2017

@author: vicio
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sea
#import urllib.request as url
#data = url.urlretrieve('ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt', "stations.txt")
file = open("stations.txt", "r")

def GNS(f):
    n = {}
    N,NS = 0,0
    for ind,line in enumerate(file):
        if "GSN" in line:
            N += 1
            #print(ind,"Station -> ",line.split())
            fields = line.split()
            n[fields[0]] = " ".join(fields[4:])
        else:
            NS += 1
    print("The number of the GSN station is {}".format(N))
    print("The number of non GSN station is {}".format(NS))
    print("The total number of station is {}".format(N+NS))
    return n
    
def findStation(nn):
    found = {cod: name for cod,name in stationNames.items() if nn in name}
    print(found)
    
stationNames = GNS(file)    

