import requests
import pandas as pd

# Example: Fetching earthquake data from USGS
usgs_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    'format': 'geojson',
    'starttime': '2020-01-01',
    'endtime': '2023-01-01',
    'minmagnitude': 4.0
}
response = requests.get(usgs_url, params=params)
earthquake_data = response.json()

# Process earthquake data
earthquake_features = []
for feature in earthquake_data['features']:
    properties = feature['properties']
    geometry = feature['geometry']['coordinates']
    earthquake_features.append([
        properties['time'], geometry[1], geometry[0], geometry[2], properties['mag']
    ])

earthquake_df = pd.DataFrame(earthquake_features, columns=['timestamp', 'latitude', 'longitude', 'depth', 'magnitude'])
earthquake_df['timestamp'] = pd.to_datetime(earthquake_df['timestamp'], unit='ms')

# Example: Fetching cosmic weather data from NOAA
# Note: Replace with actual API or data source for real implementation
# Here we mock the data for demonstration purposes
cosmic_weather_df = pd.DataFrame({
    'timestamp': pd.date_range(start='2020-01-01', periods=1000, freq='H'),
    'solar_flare_intensity': np.random.uniform(0, 10, 1000),
    'geomagnetic_index': np.random.uniform(0, 100, 1000),
    'cosmic_ray_flux': np.random.uniform(0, 1000, 1000)
})

# Merge datasets
combined_data = pd.merge(earthquake_df, cosmic_weather_df, on='timestamp')
