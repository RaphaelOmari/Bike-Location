The Bike Theft Locator is a Python application designed to help users find stolen bicycles. 
It fetches data from an online source and filters the bikes based on user-specified criteria such as location and duration since the bike was stolen. 
Additionally, the script simulates converting bike images to base64 strings and generating a PDF file with these images.

Installation:
> Before running the script, ensure that you have Python installed on your system. Additionally, the script requires a few external libraries, which can be installed via pip.
> Clone the repository or download the script file.

Install the required libraries:
    > pip install requests geopy fpdf Pillow

You will be prompted to enter the location and duration (in months) to filter the stolen bikes. 
The script will then display the filtered bike information, including a base64 encoded dummy PDF.

Features:
> Fetches and processes bike data from an online JSON source.
> Filters stolen bikes based on location and duration.
> Simulates converting images to base64 strings.
> Simulates generating a PDF with bike images.
> Displays the bike information in a user-friendly format.

Configuration:
> Modify the filtering logic in filter_by_date and format_bike_info functions as per your requirements.