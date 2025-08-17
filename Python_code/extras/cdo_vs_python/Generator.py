

import numpy as np
import xarray as xr
import pandas as pd
import os

# Settings
n_years = 20
start_year = 1990
ny = 181 *2  # lat from -90 to 90, step 1°
nx = 360 *2  # lon from -180 to 179, step 1°
out_dir = "synthetic_climate_daily"
os.makedirs(out_dir, exist_ok=True)

lat = np.linspace(-90, 90, ny)
lon = np.linspace(-180, 179, nx)  # 1 degree step, no duplicate endpoint

for year in range(start_year, start_year + n_years):
    print(f"Generating files for year {year}...")
    dates = pd.date_range(f"{year}-01-01", f"{year}-12-31", freq="D")

    base_temp = 15 + 10 * np.sin(np.deg2rad(lat))[:, None]

    for date in dates:
        day_of_year = date.dayofyear
        seasonal = 5 * np.sin(2 * np.pi * day_of_year / 365)
        noise = np.random.normal(0, 2, (ny, nx))
        temp = (base_temp + seasonal + noise).astype(np.float32)

        ds = xr.Dataset(
            {"tas": (("time", "lat", "lon"), temp[None, :, :])},  # add time dim of size 1
            coords={
                "time": ("time", [pd.Timestamp(date)], {"standard_name": "time"}),
                "lat": ("lat", lat, {"units": "degrees_north", "standard_name": "latitude"}),
                "lon": ("lon", lon, {"units": "degrees_east", "standard_name": "longitude"})
            },
            attrs={"Conventions": "CF-1.8", "title": "Synthetic daily climate data"}
        )


        filename = os.path.join(out_dir, f"temp_{date.strftime('%Y%m%d')}.nc")
        ds.to_netcdf(
            filename,
            format="NETCDF4",
            encoding={
                "time": {"units": "days since 1970-01-01", "calendar": "gregorian"},
                "tas": {"zlib": False}
            }
        )

print("✅ Daily NetCDF files generated.")

