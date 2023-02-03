import unittest
from app import app
import requests

class FlaskTestCase(unittest.TestCase):
    
    def crete_app(self):
        return app
    
    def test_classify(self):
        # Define the URL of the endpoint
        url = "http://localhost:5000/classify"

        # Define a sample row of pixels using a list comprehension
        pixels = [0 if i % 2 == 0 else 255 for i in range(28 * 28)]

        # Make a request to the API endpoint
        response = requests.post(url, json={"pixels": pixels})

        # Parse the response as a JSON object
        result = response.json()

        # Check the expected result against the actual result
        expected_result = {"class": '0'}
        
        assert result == expected_result, f"Expected {expected_result} but got {result}"
        print("Test passed!")

if __name__ == '__main__':
    unittest.main()
