import requests
import json

def get_location_url(lat, long, distance_km):
    # Construct the Google Maps URL with the specified distance
    return f"https://www.google.com/maps/search/?api=1&query={lat},{long}&radius={distance_km}km"

def find_location_within_distance(bike_data, distance_km):
    for bike in bike_data["bikes"]:
        coordinates = bike["stolen_coordinates"]
        lat, long = coordinates[0], coordinates[1]
        location_url = get_location_url(lat, long, distance_km)
        print(f"Location of the stolen bike within {distance_km}km: {location_url}")

# Define the distances you want to search (e.g., 5km and 10km)
distances_to_search = [5, 10]

for distance in distances_to_search:
    find_location_within_distance(bike_data, distance)
