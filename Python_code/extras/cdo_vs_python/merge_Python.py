"""
Created on Mon Aug 11 15:15:12 2025

@author: EMS GEA Computing
-Through Numbers the Earth
"""

import xarray as xr
import glob, time

files = sorted(glob.glob("synthetic_climate_daily/temp_*.nc"))

t0 = time.time()
ds = xr.open_mfdataset(files, combine='by_coords')
region = ds.sel(lat=slice(30, 60), lon=slice(-130, -60)).load()
mean = region.mean(dim="time").load()
print(f"Python runtime: {time.time() - t0:.2f} s")

# runcell(0, '/home/user/Documents/Gea/Dimitris/UCY2Sept/Python_code/extras/untitled3.py')
# Python runtime: 37.26 s