from sklearn.decomposition import PCA

# Create more sophisticated features
combined_data['earthquake_magnitude_avg'] = combined_data['magnitude'].rolling(window=24).mean()
combined_data['solar_flare_intensity_avg'] = combined_data['solar_flare_intensity'].rolling(window=24).mean()
combined_data['geomagnetic_index_avg'] = combined_data['geomagnetic_index'].rolling(window=24).mean()
combined_data['cosmic_ray_flux_avg'] = combined_data['cosmic_ray_flux'].rolling(window=24).mean()

# Drop NaN values
combined_data = combined_data.dropna()

# Dimensionality reduction
pca = PCA(n_components=2)
pca_features = pca.fit_transform(combined_data[['solar_flare_intensity_avg', 'geomagnetic_index_avg', 'cosmic_ray_flux_avg']])
combined_data['pca1'] = pca_features[:, 0]
combined_data['pca2'] = pca_features[:, 1]
