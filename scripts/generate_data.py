# Import libraries and functions
from scrape_website import get_products
from generate_products import generate_products
from external_data import get_emission
import json
from pandas import json_normalize
import pandas as pd

def get_carbon_from_products(list_category):
    final_df = pd.DataFrame()
    for category in list_category:
        print(category)
        df_emissions = pd.DataFrame()
        json_products = generate_products(category)
        json_data = json.loads(json_products)
        print(json_data)
        for my_data in json_data:
            print(my_data)
            df_emission = get_emission(my_data['Product name'])
            print(df_emission)
            if df_emission.empty:
                pass
            else:                
                df_emissions = pd.concat([df_emissions, df_emission])
        final_df = pd.concat([final_df, df_emissions])

    return final_df

final_df = get_carbon_from_products(get_products())
final_df.to_csv("data/emissions.csv")

