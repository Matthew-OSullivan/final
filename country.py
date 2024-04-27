# Function to fetch country data from restcountries.com API
import requests


def get_country_data(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
