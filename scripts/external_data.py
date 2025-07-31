# Import library
import pandas as pd

# Import food carbon emission data
# Data source: Poore and Nemecek (2018). 
# Poore, J., & Nemecek, T. (2018). Reducing food’s environmental impacts through producers and consumers. Science. – processed by Our World in Data
carbon_df = pd.read_csv("data/greenhouse-gas-emissions-per-kilogram-of-food-product.csv")
carbon_df.columns = ['entity', 'year', 'emission_per_kilogram']


