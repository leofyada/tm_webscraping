# Import library
import requests
from bs4 import BeautifulSoup

# Static variables
url = "https://thrivemarket.com/our-products"

# Beautiful Soup objects
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Function to get products
def get_products():
    # List to store product categories
    product_list = []
    # Get data from class that stores product categories
    product_cards = soup.select('.sc-9722c652-0.dPaEDq')
    # Loop through product categories
    for product in product_cards:
        product_list.append(product.get_text())
    # Return products
    return product_list




