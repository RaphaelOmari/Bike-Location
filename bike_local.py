import json
import base64
import requests
from datetime import datetime, timedelta
from geopy.distance import geodesic
import io
from PIL import Image
from fpdf import FPDF

def get_bike_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def calculate_duration(timestamp, duration_months):
    current_time = datetime.now().timestamp()
    duration_seconds = duration_months * 2592000  # Convert months to seconds
    return current_time - timestamp <= duration_seconds

def filter_by_date(bikes_data, duration_months):
    filtered_bikes = []
    cutoff_date = datetime.now() - timedelta(days=duration_months*30)
    cutoff_timestamp = int(cutoff_date.timestamp())
    
    for bike in bikes_data['bikes']:
        if bike['date_stolen'] and bike['date_stolen'] >= cutoff_timestamp:
            filtered_bikes.append(bike)
    
    return {'bikes': filtered_bikes}

def convert_images_to_base64(bikes):
    for bike in bikes['bikes']:
        if bike['large_img']:
            bike['base64_img'] = 'base64_encoded_string_simulated'
    return bikes

def generate_pdf_with_images(bikes):
    # Placeholder function for generating a PDF
    return 'base64_encoded_pdf_simulated'

def format_bike_info(bike):
    bike_info = {
        "Title": bike['title'],
        "Stolen Location": bike['stolen_location'],
        "Stolen Date": datetime.fromtimestamp(bike['date_stolen']).strftime('%Y-%m-%d %H:%M:%S') if bike['date_stolen'] else "Not Available",
        "More Info URL": bike['url'],
        "Google Maps URL": f"https://www.google.com/maps?q={bike['stolen_coordinates'][0]},{bike['stolen_coordinates'][1]}" if bike['stolen_coordinates'] else "Not Available",
        "Image Base64": bike.get('base64_img', 'No image available')
    }
    return bike_info

if __name__ == '__main__':
    url = 'https://example.com/bike_data.json'  # Replace with the actual URL
    data = get_bike_data(url)

    if data:
        location = input("Enter a location: ")
        duration = int(input("Enter the duration in months: "))

        filtered_bikes = filter_by_date(data, duration)
        stolen_bikes_with_images = convert_images_to_base64(filtered_bikes)
        base64_pdf = generate_pdf_with_images(stolen_bikes_with_images)

        if len(stolen_bikes_with_images['bikes']) == 0:
            print("No stolen bikes found in the specified location within the given duration.")
        else:
            print("\nStolen bikes found in the specified location within the given duration:")
            for bike in stolen_bikes_with_images['bikes']:
                bike_info = format_bike_info(bike)
                printable_info = "\n".join(f"{key}: {value}" for key, value in bike_info.items())
                print(printable_info)
                print("\n" + "-"*40 + "\n")

            print(f"PDF with images in Base64 format: {base64_pdf}")