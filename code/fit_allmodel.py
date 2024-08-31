# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:09:15 2019

@author: Administrator
"""
import h5py
from deepforest import CascadeForestRegressor
import pickle

dataFile = 'data_o3_v2.mat'
data = h5py.File(dataFile)
x_train=data['input'][:].T
y_train=data['y'][:].T
    
gbm=CascadeForestRegressor(max_layers=10, n_trees=100, n_estimators=2, max_depth=30, 
                           use_predictor=False,n_jobs=28)
    
gbm.fit(x_train,y_train)
gbm.save('all_model')