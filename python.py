import pandas as pd

neighborhood_atlas = pd.read_csv('https://ahistorage.blob.core.windows.net/507/Neighborhood_atlas.csv')

SPARCS = pd.read_json('https://health.data.ny.gov/resource/82xm-y6g8.json')

##checking columns
SPARCS.columns 
neighborhood_atlas.columns


###clean columns
SPARCS.columns = SPARCS.columns.str.replace('[^A-Za-z0-9]+', '_')

neighborhood_atlas.columns = neighborhood_atlas.columns.str.replace('[^A-Za-z0-9]+', '_')

SPARCS.columns = SPARCS.columns.str.lower()

neighborhood_atlas.columns = neighborhood_atlas.columns.str.lower()

###checking column types

SPARCS.dtypes

neighborhood_atlas.dtypes


## create smaller dataframes

df_sparcs_small = SPARCS[[
    'hospital_county',
    'facility_name',
    'age_group',
    'gender',
    'race',
    'zip_code_3_digits'
]]
print(df_sparcs_small.sample(10).to_markdown())

df_sparcs_small.shape

df_neighborhood_atlas_small = neighborhood_atlas[[
    'type',
    'zipid',
    'adi_natrank']]

print(df_neighborhood_atlas_small.sample(10).to_markdown())

###merge

combined_df = df_sparcs_small.merge(df_neighborhood_atlas_small, how='left', left_on='zip_code_3_digits', right_on='zipid')
combined_df = pd.merge(df_sparcs_small, df_neighborhood_atlas_small, how='left', left_on='zip_code_3_digits', right_on='zipid')

combined_df.shape

##saved combined df to csv
combined_df.to_csv('combined_data.csv')

