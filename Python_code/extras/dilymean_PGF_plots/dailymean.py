"""
Created on Fri Aug 15 10:15:35 2025
@author: EMS GEA Computing
- Through Numbers the Earth
"""

# -----------------------------
# Import necessary libraries
# -----------------------------
import xarray as xr           # For working with multi-dimensional datasets (like NetCDF)
import matplotlib.pyplot as plt  # For plotting data
import numpy as np           # For numerical operations (min, max, mean, etc.)

# -----------------------------
# Load sample dataset
# -----------------------------
# Use xarray's tutorial dataset "air_temperature" and select only the 'air' variable
ds = xr.tutorial.open_dataset("air_temperature")['air']

# -----------------------------
# Configuration variables
# -----------------------------
aggr = True   # Boolean flag: True → aggregate over all lon/lat, False → select a specific point

# Coordinates for point selection (used if aggr=False)
lon, lat = -77, 40

# -----------------------------
# Subset or aggregate dataset
# -----------------------------
if aggr:
    # Compute the mean over all longitudes and latitudes → reduce spatial dimensions
    ds = ds.mean(dim=['lon','lat'])
else:
    # Adjust longitudes from 0-360 to -180 to 180 for easier selection
    ds.coords['lon'] = (ds.coords['lon'] + 180) % 360 - 180
    # Select nearest grid point to specified latitude and longitude
    ds = ds.sel(lat=lat, lon=lon, method='nearest')

# -----------------------------
# Prepare plotting
# -----------------------------
plt.close('all')  # Close any previous plots to avoid overlap


# -----------------------------
# Set metadata attributes for clarity
# -----------------------------
ds.attrs['long_name'] = 'Air Temperature'  # Descriptive variable name
ds.attrs['short_name'] = 'air temp'       # Short label
ds.attrs['units'] = 'K'                   # Original units (Kelvin), could also be updated to 'C'




# -----------------------------
# Convert units from Kelvin to Celsius
# -----------------------------
if True:  # Always execute
    ds = ds - 273.15       # Convert temperature to Celsius
    ds.attrs['units'] = 'C'  # Update units metadata


# -----------------------------
# Define aggregations and plotting styles
# -----------------------------
# Dictionary maps each aggregation type to:
#   1. The function to apply (np.min, np.mean, np.max)
#   2. Plotting color, line width, and transparency (alpha)
agg_dict = {
    'min':  {'func': np.min,  'color': 'orange', 'linewidth': 1, 'alpha': 0.5},
    'mean': {'func': np.mean, 'color': 'red',  'linewidth': 2, 'alpha': 0.9},
    'max':  {'func': np.max,  'color': 'blue', 'linewidth': 1, 'alpha': 0.5}
}

# -----------------------------
# Loop over each aggregation type and plot
# -----------------------------
for name, props in agg_dict.items():
    # Group data by day of year (1-366) and apply aggregation function
    # This allows plotting seasonal cycles (min, mean, max for each day)
    ds.groupby('time.dayofyear').reduce(props['func']).plot(
        label=name,                 # Label for legend
        color=props['color'],       # Line color
        linewidth=props['linewidth'], # Line thickness
        alpha=props['alpha']        # Transparency for visual layering
    )

# -----------------------------
# Add legend and grid for clarity
# -----------------------------
plt.legend()  # Show labels for each aggregation
plt.grid()    # Add grid lines for easier reading
plt.xlim(0, 365)


# -----------------------------
# Add appropriate plot title
# -----------------------------
if aggr:
    plt.title("Aggregated over all lats and lons")  # Spatially averaged plot
else:
    plt.title(f"Selected lon: {lon}, lat: {lat}")   # Single point plot

# -----------------------------
# Display the plot
# -----------------------------
plt.show()









import pandas as pd
daily_group = ds.groupby('time.dayofyear')

# -----------------------------
# Compute daily min, mean, max
# -----------------------------
daily_min = daily_group.reduce(np.min)
daily_mean = daily_group.reduce(np.mean)
daily_max = daily_group.reduce(np.max)

# -----------------------------
# Combine into a pandas DataFrame
# -----------------------------
df = pd.DataFrame({
    'day': daily_min['dayofyear'].values,
    'min': daily_min.values,
    'mean': daily_mean.values,
    'max': daily_max.values
})

df.to_csv('daily_air_temperature.csv', index=False)

print("CSV file 'daily_air_temperature.csv' created successfully!")





