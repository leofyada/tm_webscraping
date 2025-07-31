# Import libraries and functions
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env variables into environment
load_dotenv()
# Access OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API"))

# Function to get products based on product categories
def generate_products(category):
    prompt = f"""
    Generate 5 generic grocery products commonly found in the category "{category}".
    Each product should have a generic name (e.g., "almond butter", "whole wheat pasta") that can be matched with carbon footprint databases.

    For each product, return:
    - 'Product name': a generic name without brand
    - 'Typical unit/quantity': a realistic package size (e.g., 500g, 1 lb)
    - 'Main ingredients': key components that determine the product type
    - 'Category': reuse the input category

    Format your response as a JSON list. Do not use line breaks.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


