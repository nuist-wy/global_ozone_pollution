# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:09:15 2019

@author: Administrator
"""
import scipy.io as scio
import numpy as np
import pickle
import os
from natsort import natsorted
import h5py
import warnings

warnings.filterwarnings('ignore')

tem = h5py.File('gen_template.mat')
flag=tem['flag'][:].T
se=tem['se'][:]
nw1=tem['nw1'][:].T
nw2=tem['nw2'][:].T

gbms=[]
adm=r'F:\sitemodel\gen'
sdir=natsorted(os.listdir(adm))
for filename in sdir:
    pathm=os.path.join(adm,filename)
    fw = open(pathm,'rb')
    gbms.append(pickle.load(fw))
    fw.close()

ad=r'F:\input_c'
ads=r'F:\site_output_v2'
adr=r'F:\output_v2c'
    
for filename in os.listdir(ad):
    path=os.path.join(ad,filename)
    pathr=os.path.join(adr,filename)
    paths=os.path.join(ads,filename)
    print(paths)
    data = h5py.File(path)
    repd = scio.loadmat(pathr)
    x_test=data['par'][:].T
    x_test=np.delete(x_test,np.arange(21,24),1)
    nx_test=np.delete(x_test,np.arange(10,18),1)
    bound=data['bound'][:].T
    rep=repd['ypreda'].ravel()
    
    cou=0
    tcou=len(rep)
    ypredf=np.zeros((tcou,)) 
    
    for ele in bound:
        if cou%10000==0:
            print(cou/tcou*100)
        cc=int(ele[0]-1)
        rr=int(ele[1]-1)
        set=se[:,rr,cc]
        if flag[cc,rr]==0:
            ypred=rep[cou]
        else:
            ypreds=0 
            for k in range(0,len(set)):
                ypred_=gbms[int(set[k])-1].predict(nx_test[cou].reshape(1, -1))
                ypreds=ypreds+ypred_*0.1
            if flag[cc,rr]==1:
                ypred=ypreds*nw1[cc,rr]+rep[cou]*nw2[cc,rr]
            else:
                ypred=ypreds
        ypredf[cou]=ypred
        cou=cou+1
    ypredf = np.where(ypredf < 0,rep,ypredf)
    scio.savemat(paths,{'ypredf':ypredf})