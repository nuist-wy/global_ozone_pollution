# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:09:15 2019

@author: Administrator
"""
import scipy.io as scio
import h5py
import sys
import numpy as np
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from deepforest import CascadeForestRegressor
import math
import sklearn.metrics as m

r=[]
y=[]
x=np.empty((1,0))
lo1=np.empty((1,0))
lo2=np.empty((1,0))
yy=np.empty((1,0))
mm=np.empty((1,0))
for ind in range(1,6):
    dataFile = 'o3_ind.mat'
    dataFile=dataFile.replace('ind',str(ind))
    datasave = 'all_ind.model'
    datasave=datasave.replace('ind',str(ind))
    data = h5py.File(dataFile)
    x_train=data['trindata'][:].T.astype('float32')
    y_train=data['troutdata'][:].T.astype('float32')
    x_test=data['teindata'][:].T.astype('float32')
    y_test=data['teoutdata'][:].T.astype('float32')
    lotest=data['lotest'][:].T
    tstest=data['tstest'][:].T
    
    
    gbm=LGBMRegressor(objective='regression',num_leaves=2048,max_depth=12,learning_rate=0.1,n_estimators=800,
                         # colsample_bytree=0.8,subsample=0.8,n_jobs=28)
    
    # gbm=CascadeForestRegressor(max_layers=10, n_trees=100, n_estimators=2, max_depth=30,
                            # use_predictor=False, predictor="xgboost",n_jobs=28)
    
    # gbm=XGBRegressor(n_estimators=800,subsample=0.8,max_depth=12,colsample_bytree=0.8 ,min_child_weight=3,max_leaves=2048,
                           # importance_type='gain',n_jobs=28,gamma=0,reg_lambda=2,learning_rate=0.1,tree_method="hist")
    # gbm=RandomForestRegressor(max_depth=30,n_estimators=150,n_jobs=28)
    # gbm=ExtraTreesRegressor(max_depth=30,n_estimators=150,n_jobs=28)
    
    gbm.fit(x_train,y_train)

    ypred = gbm.predict(x_test).ravel()
    r.append(np.corrcoef(y_test.T, ypred)[0, 1])
    print(np.corrcoef(y_test.T, ypred)[0, 1])
    x=np.concatenate((x,y_test.T),axis = 1)
    y.extend(ypred)
    lo1=np.concatenate((lo1,lotest[:,0].reshape(1,-1)),axis = 1)
    lo2=np.concatenate((lo2,lotest[:,1].reshape(1,-1)),axis = 1)
    yy=np.concatenate((yy,tstest[:,0].reshape(1,-1)),axis = 1)
    mm=np.concatenate((mm,tstest[:,1].reshape(1,-1)),axis = 1)

print(np.corrcoef(x,y)[0, 1])
print(math.sqrt(m.mean_squared_error(x.T,y)))
scio.savemat('point_lgbm_v2.mat', {'x':x.T,'y':y,'lo1':lo1,'lo2':lo2,'yy':yy,'mm':mm})