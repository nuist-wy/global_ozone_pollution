# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:09:15 2019

@author: Administrator
"""
import scipy.io as scio
import numpy as np
import pickle
import sklearn.metrics as m
import math
import os
import h5py

y=[]
x=np.empty((1,0))
lo1=np.empty((1,0))
lo2=np.empty((1,0))
yy=np.empty((1,0))
mm=np.empty((1,0))
adt=r'F:\testdata\ind_t'
adt_=r'F:\sitemodel\ind_t'
filename_allt='all_ind_t.model'

for ind in range(1,6):
    ad=adt.replace('ind', str(ind))
    ad_=adt_.replace('ind', str(ind))
    filename_all=filename_allt.replace('ind', str(ind))
    fw = open(filename_all,'rb')
    gbma = pickle.load(fw)
    fw.close()
    
    for filename in os.listdir(ad):
        path=os.path.join(ad,filename)
        
        data = h5py.File(path)
        x_test=data['inputf'][:].T
        nx_test=np.delete(x_test,np.arange(10,18),1)
        y_test=data['yf'][:].T
        coord = data['coord'][:].T
        yymm=data['yymm'][:].T
        se=data['se'][:]
        ws=data['weights'][:]
        flag=data['flag'][:][0]
        nw1=data['nw1'][:][0]
        nw2=data['nw2'][:][0]
        
        y_test=y_test.T.tolist()
        
        ypreda=gbma.predict(x_test).ravel()
        
        if flag==0:
            ypred=ypreda
        else:
            ypreds=np.zeros((len(y_test),)) 
            for k in range(0,len(se)):
                filename_=str(int(se[k]))+'.model'
                fw = open(os.path.join(ad_,filename_),'rb')
                gbm = pickle.load(fw)
                fw.close()
                ypred_=gbm.predict(nx_test)
                ypred_=np.array(ypred_)*0.1
                ypreds=ypreds+ypred_
            if flag==1:
                ypred=ypreds*nw1+ypreda*nw2
            else:
                ypred=ypreds
        ypred=np.where(ypred<0,ypreda,ypred)
        lo1 = np.concatenate((lo1, coord[:, 0].reshape(1, -1)), axis=1)
        lo2 = np.concatenate((lo2, coord[:, 1].reshape(1, -1)), axis=1)
        yy = np.concatenate((yy, yymm[:, 0].reshape(1, -1)), axis=1)
        mm = np.concatenate((mm, yymm[:, 1].reshape(1, -1)), axis=1)
        x=np.concatenate((x,y_test),axis = 1)
        y.extend(ypred)
    del gbma
print(np.corrcoef(x,y)[0, 1])
print(math.sqrt(m.mean_squared_error(x.T,np.array(y))))
scio.savemat('point_gl_t_v2.mat', {'x':x.T,'y':y,'lo1':lo1,'lo2':lo2,'yy':yy,'mm':mm})
