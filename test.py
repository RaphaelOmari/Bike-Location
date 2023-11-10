import unittest
from datetime import datetime
from unittest.mock import patch
from bike_local import find_stolen_bikes, calculate_distance, show_on_google_maps

class TestBikeFinder(unittest.TestCase):
    def test_find_stolen_bikes(self):
        location = "London, UK"
        duration = 3  # 3 months
        example_data = {
            "bikes": [
                {
                    "status": "stolen",
                    "stolen_location": "London, UK",
                    "date_stolen": datetime.now().timestamp() - (30 * 24 * 3600 * duration)
                },
                {
                    "status": "stolen",
                    "stolen_location": "Manchester, UK",
                    "date_stolen": datetime.now().timestamp() - (30 * 24 * 3600 * duration)
                },
                {
                    "status": "stolen",
                    "stolen_location": "Edinburgh, UK",
                    "date_stolen": datetime.now().timestamp() - (30 * 24 * 3600 * duration)
                },
            ]
        }

        with patch('your_script.get_bike_data', return_value=example_data):
            stolen_bikes = find_stolen_bikes(location, duration)
            self.assertEqual(len(stolen_bikes), 2)
            self.assertIn("London, UK", [bike['stolen_location'] for bike in stolen_bikes])
            self.assertNotIn("Manchester, UK", [bike['stolen_location'] for bike in stolen_bikes])

    def test_calculate_distance(self):
        coords1 = (51.509865, -0.118092)  # London
        coords2 = (55.953251, -3.188267)  # Edinburgh

        distance = calculate_distance(coords1, coords2)
        self.assertAlmostEqual(distance, 536.47, places=2)  # Approx 536km between London to Edinburgh

    def test_show_on_google_maps(self):
        coords = (51.509865, -0.118092)  # London
        map_url = show_on_google_maps(coords)
        self.assertIn("https://www.google.com/maps?q=51.509865,-0.118092", map_url)

if __name__ == '__main__':
    unittest.main()