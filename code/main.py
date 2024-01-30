import netCDF4 as nc
import matplotlib.pyplot as plt
import os
import numpy as np

file_dir = r'D:\data'
files = os.listdir(file_dir)


for i in range(0, files.__len__(), 1):
    filename=file_dir + '/' + files[i]
    Data=nc.Dataset(filename)
	
    data_o3=np.array(Data.variables['ambient_ozone'])
    lats=np.array(Data.variables['Latitude'])
    lons=np.array(Data.variables['Longitude'])
    
    plt.contourf(lons,lats,data_o3,256)
    plt.colorbar(label='ambient ozone concentrations (ppb)',orientation='horizontal')
    plt.show()