import netCDF4 as nc
import numpy as np
import datetime

def convert_to_nc(filename, cur_date, data_o3):
    data_o3[data_o3==0]=np.nan

    gridspi=nc.Dataset(filename, 'w', format='NETCDF4')
    # dimensions
    gridspi.createDimension('Latitude', 3600)
    gridspi.createDimension('Longitude', 7200)
    # Create coordinate variables for dimensions
    latitudes=gridspi.createVariable('Latitude', np.float32, ('Latitude'))
    longitudes=gridspi.createVariable('Longitude', np.float32, ('Longitude'))

    # Variable Attributes
    latitudes.units='degree_north'
    longitudes.units='degree_east'
    
    # data
    lats=np.arange(90 - 0.05 / 2, -90, -0.05)  # notice: the last numb is not included
    lons=np.arange(-180 + 0.05 / 2, 180, 0.05)  # notice: the last numb is not included
    latitudes[:]=lats
    longitudes[:]=lons

    data=gridspi.createVariable('ambient_ozone', np.float32, ('Latitude', 'Longitude'))
    data[:]=data_o3.astype(np.float32)
    data.long_name="Maximum daily 8-hour averaged ambient ozone concentrations"
    data.units='parts per billion'
    data.coordinates='Longitude Latitude'
    data.origname='ambient_ozone'
    data.fullnamepath='/ambient_ozone'

    gridspi.date=cur_date
    gridspi.source='netCDF4 python module tutorial'
    gridspi.reference='Unrevealed significant global health risks of current ozone pollution'
    #gridspi.url=''
    gridspi.time_stamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gridspi.author='Yuan Wang, NUIST'
    gridspi.close()

    return