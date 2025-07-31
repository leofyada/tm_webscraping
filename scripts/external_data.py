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
# Access Climatiq API key
MY_API_KEY = os.getenv("API_KEY")
# Endpoing
url = "https://api.climatiq.io/data/v1/search"

# Function to get carbon emission estimate
def get_emission(query):
    # Completely empty to store carbon emissiondata 
    df = pd.DataFrame()
    # Parameters
    data_version = "^3"
    query_params = {
        # Free text query can be written as the "query" parameter
        "query": query,
        "data_version": data_version,
        # You can also filter on region, year, source and more
        # "AU" is Australia
        #"region": "AU"
    }
    # You must always specify your AUTH token in the "Authorization" header like this.
    authorization_headers = {"Authorization": f"Bearer {MY_API_KEY}"}

    try:
        # This performs the request and returns the result as JSON
        response = requests.get(url, params=query_params, headers=authorization_headers).json()
        # And here you can do whatever you want with the results
        for result in response['results']:
            
            # === Top-level fields ===
            activity_id = result['activity_id']
            material_id = result['id']
            name = result['name']
            category = result['category']
            sector = result['sector']
            source = result['source']
            source_link = result['source_link']
            source_dataset = result['source_dataset']
            uncertainty = result['uncertainty']
            year = result['year']
            year_released = result['year_released']
            region = result['region']
            region_name = result['region_name']
            description = result['description']
            unit_type = result['unit_type']
            unit = result['unit']
            source_lca_activity = result['source_lca_activity']
            data_quality_flags = result['data_quality_flags']
            access_type = result['access_type']
            supported_calculation_methods = result['supported_calculation_methods']
            factor = result['factor']
            factor_calculation_method = result['factor_calculation_method']
            factor_calculation_origin = result['factor_calculation_origin']

            # === Nested fields ===
            constituent_gases = result.get('constituent_gases', {})
            co2e_total = constituent_gases.get('co2e_total')
            co2e_other = constituent_gases.get('co2e_other')
            co2 = constituent_gases.get('co2')
            ch4 = constituent_gases.get('ch4')
            n2o = constituent_gases.get('n2o')

            data_version = result.get('data_version', {})
            data_version_status = data_version.get('status')

            data_version_info = result.get('data_version_information', {})
            data_version_info_status = data_version_info.get('status')


            data = [{            
                "type" : type,
                "query" : query,
                "activity_id" : activity_id,
                "material_id" : material_id,
                "name" : name,
                "category" : category,
                "sector" : sector,
                "source" : source,
                "source_link" : source_link,
                "source_dataset" : source_dataset,
                "uncertainty" : uncertainty,
                "year" : year,
                "year_released" : year_released,
                "region" : region,
                "region_name" : region_name,
                "description" : description,
                "unit_type" : unit_type,
                "unit" : unit,
                "source_lca_activity" : source_lca_activity,
                "data_quality_flags" : data_quality_flags,
                "access_type" : access_type,
                "supported_calculation_methods" : supported_calculation_methods,
                "factor" : factor,
                "factor_calculation_method" : factor_calculation_method,
                "factor_calculation_origin" : factor_calculation_origin,
                "constituent_gases" : constituent_gases,
                "co2e_total" : co2e_total,
                "co2e_other" : co2e_other,
                "co2" : co2,
                "ch4" : ch4,
                "n2o" : n2o,
                "data_version" : data_version,
                "data_version_status" : data_version_status,
                "data_version_info" : data_version_info,
                "data_version_info_status" : data_version_info_status}]
            
            df_material = pd.DataFrame(data)
            
            if df_material.empty:
                return None
            else:
                df = pd.concat([df, df_material])

        return df
    
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error occurred: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection error occurred: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error occurred: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    except ValueError:
        print("Failed to parse response as JSON.")
    except KeyError:
        print("Emission not found")
    
    return None

