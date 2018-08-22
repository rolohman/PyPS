#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:20:01 2018
  Make dates and pairs dictionaries

@author: kdm95
"""
import numpy as np
import glob
import pickle
from osgeo import gdal

#<><><><><><><><><><><><>Set these variables><><><><><><><><><><><><><><><
# Define area of interest
workdir = '/data/rlohman/Sentinel/Saudi/28_67_stack/' # working directory (should be where merged is)
alks = int(3) # number of looks in azimuth
rlks = int(7) # number of looks in range
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><

lam = 0.056 # 0.056 for c-band
mergeddir = workdir + 'merged/'
slcdir    = workdir + 'SLC/'
intdir    = mergeddir + 'interferograms/'
tsdir     = workdir + 'TS/'

dates = list()
flist = glob.glob(slcdir + '2*')
[dates.append(f[-8:]) for f in flist]
dates.sort();

f_lon = mergeddir + 'geom_master/lon.rdr.vrt'
lon_ifg = gdal.Open(f_lon).ReadAsArray()

# Image dimensions before and after downlooking
nd = len(pairs) # number of pairs (number of dates minus one?)
ny,nx = lon_ifg.shape
nxl = int(np.floor(nx/rlks))
nyl = int(np.floor(ny/alks))

print ("Number of dates found: "+str(nd))

# Saving the objects:
with open(tsdir + 'params.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump([dates,nd,lam,workdir,slcdir,intdir,tsdir,ny,nx,nxl,nyl,alks,rlks], f)

del(lon_ifg)
