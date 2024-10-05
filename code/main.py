import pandas as pd

url_table_loc = "../sources/rare-disease_cleaned.AUG.2024.csv"

urls_df = pd.read_csv(url_table_loc)

print(urls_df.head())