import pandas as pd

cities_education = pd.read_csv('../DATA/Education/cityTotalSchools.csv')
health = pd.read_csv('../DATA/Healthcare/numberofHospitals.csv')
health2 = pd.read_csv('../DATA/Healthcare/numberOfPharmecies.csv')
merge_df = pd.merge(cities_education, health, on='city', how='left').reset_index()
merge_df.fillna(0, inplace=True)
merge_df = pd.merge(merge_df, health2, on='city', how='left').reset_index()
merge_df.fillna(0, inplace=True)
merge_df.to_csv('table.csv', index=False)