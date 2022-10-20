import pandas as pd

neighborhood_atlas = pd.read_csv('https://ahistorage.blob.core.windows.net/507/Neighborhood_atlas.csv')

SPARCS = pd.read_json('https://health.data.ny.gov/resource/82xm-y6g8.json')