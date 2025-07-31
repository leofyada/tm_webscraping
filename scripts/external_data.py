# Import library
import pandas as pd
import requests
from dotenv import load_dotenv
import os

# Import food carbon emission data
# Data source: Poore and Nemecek (2018). 
# Poore, J., & Nemecek, T. (2018). Reducing food’s environmental impacts through producers and consumers. Science. – processed by Our World in Data
carbon_df = pd.read_csv("data/greenhouse-gas-emissions-per-kilogram-of-food-product.csv")
carbon_df.columns = ['entity', 'year', 'emission_per_kilogram']

# Get data from Climatiq
# Load .env variables into environment
load_dotenv()
# Access your API key
MY_API_KEY = os.getenv("API_KEY")

url = "https://api.climatiq.io/data/v1/search"
query="Beverages"
data_version = "^3"

query_params = {
    # Free text query can be written as the "query" parameter
    "query": query,
    "data_version": data_version,
    # You can also filter on region, year, source and more
    # "AU" is Australia
    "region": "AU"
}

# You must always specify your AUTH token in the "Authorization" header like this.
authorization_headers = {"Authorization": f"Bearer {MY_API_KEY}"}
# This performs the request and returns the result as JSON
response = requests.get(url, params=query_params, headers=authorization_headers).json()
# And here you can do whatever you want with the results
print(response)