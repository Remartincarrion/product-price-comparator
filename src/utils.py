import requests
from difflib import SequenceMatcher

def fetch_external_data():
    url = "http://127.0.0.1:8000/products"

    try: 
        # Send Http request to url
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching external data: {e}")
        return None


def similarity(a, b):
    # Calculate the similarity between two strings
    return SequenceMatcher(None, a, b).ratio()