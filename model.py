from xgboost import XGBRegressor

# Define features and targets
features = ['pca1', 'pca2']
target_earthquake = 'magnitude'
target_cosmic_weather = 'geomagnetic_index_avg'

# Split data into training and testing sets
X = combined_data[features]
y_earthquake = combined_data[target_earthquake]
y_cosmic_weather = combined_data[target_cosmic_weather]

X_train, X_test, y_earthquake_train, y_earthquake_test = train_test_split(X, y_earthquake, test_size=0.2, random_state=42)
_, _, y_cosmic_weather_train, y_cosmic_weather_test = train_test_split(X, y_cosmic_weather, test_size=0.2, random_state=42)

# Train the earthquake prediction model
earthquake_model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
earthquake_model.fit(X_train, y_earthquake_train)

# Train the cosmic weather prediction model
cosmic_weather_model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
cosmic_weather_model.fit(X_train, y_cosmic_weather_train)

# Make predictions
y_earthquake_pred = earthquake_model.predict(X_test)
y_cosmic_weather_pred = cosmic_weather_model.predict(X_test)

# Evaluate the models
mse_earthquake = mean_squared_error(y_earthquake_test, y_earthquake_pred)
mse_cosmic_weather = mean_squared_error(y_cosmic_weather_test, y_cosmic_weather_pred)

print(f'Earthquake Model MSE: {mse_earthquake}')
print(f'Cosmic Weather Model MSE: {mse_cosmic_weather}')
