# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:51:33 2023

@author: Administrator
"""
import scipy.io as scio
import pickle
from lightgbm import LGBMRegressor
import os
import shutil
import math
import numpy as np
import h5py

path = r'F:\sitedata\gen'
path_= r'F:\sitemodel\gen'

if os.path.exists(path_):
    shutil.rmtree(path_)
os.makedirs(path_)

for filename in os.listdir(path):
    ad=os.path.join(path,filename)
    ad_=os.path.join(path_,filename.replace('mat', 'model'))
    file=h5py.File(ad)
    xtrain=file['inputf'][:].T
    xtrain=np.delete(xtrain,np.arange(10,18),1)
    ytrain=file['yf'][:].T
    intrep=file['intrep'][:][0]
    ll=len(ytrain)
    if intrep:
        gbm=LGBMRegressor(objective='regression',num_leaves=256,max_depth=int(math.log2(256)),learning_rate=0.1,n_estimators=50,
                    colsample_bytree=0.8,subsample=0.8,n_jobs=28)
    else:
        if ll<5000:
            nl=int((ll-300)/(5000-300)*(1024-256)+256)
            ne=int((ll-300)/(5000-300)*(600-50)+50)
            gbm=LGBMRegressor(objective='regression',num_leaves=nl,max_depth=int(math.log2(nl)),learning_rate=0.1,n_estimators=ne,
                        colsample_bytree=0.8,subsample=0.8,n_jobs=28)
        else:
            gbm=LGBMRegressor(objective='regression',num_leaves=1024,max_depth=int(math.log2(1024)),learning_rate=0.1,n_estimators=600,
                        colsample_bytree=0.8,subsample=0.8,n_jobs=28)
    gbm.fit(xtrain,ytrain)
    fw = open(ad_,'wb')
    pickle.dump(gbm,fw)
    fw.close()