import os
import requests


def fetch_quote():
    response = requests.get(os.environ.get('Mashape_API_Endpoint'),
    headers = {
           'x-rapidapi-key': os.environ.get('x-rapidapi-key'),
           'Accept': 'application/json',
           'x-rapidapi-host': "quotes15.p.rapidapi.com",
           
        }
    )
    if response.status_code == 200:
        return response.json()[0]

    return response.json()


