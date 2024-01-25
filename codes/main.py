import netCDF4 as nc
import matplotlib.pyplot as plt
import os

file_dir = r'D:/Data examples/'
files = os.listdir(file_dir)


for i in range(0, files.__len__(), 1):
    filename=file_dir + '/' + files[i]
    Data=nc.Dataset(filename)
	
    data_o3=Data.variables['ambient_ozone']
    lats=Data.variables['Latitude']
    lons=Data.variables['Longitude']
    
    plt.contour(lons,lats,data_o3)
    plt.colorbar(label='ambient ozone concentrations',orientation='horizontal')
    plt.show()