import numpy as np
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

# Function to calculate Haversine distance between two points
def haversine_dist(lat1, lon1, lat2, lon2):

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 3958.8 * c  # Radius of earth in miles

    return distance

# Function to calculate distance and create a new column
def calc_dist(row):
    return haversine_dist(row['pickup_latitude'], row['pickup_longitude'],
                              row['dropoff_latitude'], row['dropoff_longitude'])

# Load data
dataset = np.load("nyc_taxi_data.npy", allow_pickle=True).item()
X_train, y_train, X_test, y_test = dataset["X_train"], dataset["y_train"], dataset["X_test"], dataset["y_test"]

# Convert pickup and dropoff datetime to datetime format
X_train['pickup_datetime'] = pd.to_datetime(X_train['pickup_datetime'])
X_train['dropoff_datetime'] = pd.to_datetime(X_train['dropoff_datetime'])

# Extract month, day, and hour from pickup and dropoff datetime
X_train['pickup_month'] = X_train['pickup_datetime'].dt.month
X_train['pickup_day'] = X_train['pickup_datetime'].dt.day
X_train['pickup_hour'] = X_train['pickup_datetime'].dt.hour
X_train['dropoff_month'] = X_train['dropoff_datetime'].dt.month
X_train['dropoff_day'] = X_train['dropoff_datetime'].dt.day
X_train['dropoff_hour'] = X_train['dropoff_datetime'].dt.hour

# Calculate distance and add as a new feature
X_train['distance'] = X_train.apply(calc_dist, axis=1)

# Drop unnecessary columns
X_train.drop(columns=['id','vendor_id','pickup_datetime', 'dropoff_datetime', 'pickup_longitude', 'pickup_latitude',
                      'dropoff_longitude', 'dropoff_latitude', 'store_and_fwd_flag'], inplace=True)
X_train.info()
print(X_train.columns)

X_test['pickup_datetime'] = pd.to_datetime(X_test['pickup_datetime'])
X_test['dropoff_datetime'] = pd.to_datetime(X_test['dropoff_datetime'])

X_test['pickup_month'] = X_test['pickup_datetime'].dt.month
X_test['pickup_day'] = X_test['pickup_datetime'].dt.day
X_test['pickup_hour'] = X_test['pickup_datetime'].dt.hour
X_test['dropoff_month'] = X_test['dropoff_datetime'].dt.month
X_test['dropoff_day'] = X_test['dropoff_datetime'].dt.day
X_test['dropoff_hour'] = X_test['dropoff_datetime'].dt.hour

X_test['distance'] = X_test.apply(calc_dist, axis=1)

X_test.drop(columns=['id','vendor_id', 'pickup_datetime', 'dropoff_datetime', 'pickup_longitude', 'pickup_latitude',
                      'dropoff_longitude', 'dropoff_latitude', 'store_and_fwd_flag'], inplace=True)

X_test.info()

print(" Data Preprocessing finished ")