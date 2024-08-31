# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:33:01 2023

@author: Administrator
"""
import pickle
import os
import scipy.io as scio
import h5py
import numpy as np
from deepforest import CascadeForestRegressor

ad=r'F:\match_o3\input'
ads=r'F:\output_V2'

gbma=CascadeForestRegressor()
gbma.load('all_model')

for filename in os.listdir(ad):
    path=os.path.join(ad,filename)
    paths=os.path.join(ads,filename)
    data = h5py.File(path)
    x_test=data['par'][:].T
    ypreda=gbma.predict(np.delete(x_test,np.arange(21,24),1))
    scio.savemat(paths, {'ypreda':ypreda})