import json
from datetime import datetime
import requests
from geopy.distance import geodesic

# Retrived JSON data from 
def get_bike_data():
    url = 'https://example.com/bike_data.json'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

data = get_bike_data() #Stores the variable data as the JSON values from the API URL

if data:
    def calculate_duration(timestamp, duration):
        current_time = datetime.now().timestamp()
        return current_time - timestamp <= duration

    def find_stolen_bikes(location, duration):
        location = location.lower()
        duration_seconds = duration*2592000  # Convert months to seconds (24hours x 30days x 3600seconds)

        stolen_bikes = []

        for bike in data['bikes']:
            if bike['status'] == 'stolen' and bike['stolen_location'].lower().find(location) != -1: #The condition "find(location) != -1" checks to see if the locatiopn is found within "bike['stolen_location']" is found or not
                if bike['date_stolen'] and calculate_duration(bike['date_stolen'], duration_seconds):
                    stolen_bikes.append(bike)

        return stolen_bikes

    def show_on_google_maps(coords):
        lat, lon = coords
        map_url = f"https://www.google.com/maps?q={lat},{lon}" #Displays the google maps image of the aquired co-ordinates
        return map_url

    def calculate_distance(coords1, coords2):
        return geodesic(coords1, coords2).kilometers
    
    if __name__ == '__main__':
        location = input("Enter a location: ")
        duration = int(input("Enter the duration in months: "))

        stolen_bikes = find_stolen_bikes(location, duration)

        if len(stolen_bikes) == 0:
            print("No stolen bikes found in the specified location within the given duration.")
        else:
            print("Stolen bikes found in the specified location within the given duration:")
            for bike in stolen_bikes:
                print(f"Title: {bike['title']}")
                print(f"Stolen Location: {bike['stolen_location']}")
                print(f"Stolen Date: {datetime.fromtimestamp(bike['date_stolen']).strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"More Info: {bike['url']}")
                print(f"Distance to Location: {calculate_distance(bike['stolen_coordinates'], (lat, lon))} km")
                print(f"View on Google Maps: {show_on_google_maps(bike['stolen_coordinates'])}")
                print("")
                print("")