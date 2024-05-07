from unittest import result
from numpy import NaN
import pandas as pd
#from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
city_rental = pd.read_csv('cityRentals.csv')
city_rental = city_rental.groupby(by=['Name', 'Beds']).mean().reset_index()
print(city_rental.head())
#since our data is 
#        Name  Beds        Price
# 0    Aachen     1  1622.333333
# 1    Aachen     3  2109.500000
# 2  Augsburg     1  1723.875000
# 3  Bensheim     2  1590.000000
# 4    Berlin     1  1797.920455
#some city have data for only 1 bedrooms and not all available bedrooms
#since it has been scraped from a posting website
#so We are going to use a technique call imputation to fill up those empty spaces
# Create a DataFrame with all combinations of cities and beds
#info resource: https://scikit-learn.org/stable/modules/impute.html
cities = city_rental['Name'].unique()
all_beds = range(1, 7)
all_combinations = [(city, bed) for city in cities for bed in all_beds]
all_df = pd.DataFrame(all_combinations, columns=['Name', 'Beds'])

# Merge the original DataFrame with the DataFrame of all combinations
merged_df = pd.merge(city_rental, all_df, on=['Name', 'Beds'], how='right')

# Sort the DataFrame
merged_df.sort_values(by=['Name', 'Beds'], inplace=True)

# Display the result
print(merged_df)
#now data frame is in this format
# Name  Beds        Price
# 0       Aachen     1  1622.333333
# 1       Aachen     2          NaN
# 2       Aachen     3  2109.500000
# 3       Aachen     4          NaN
# 4       Aachen     5          NaN
# ..         ...   ...          ...
# 355  Wuppertal     2  1807.666667
# 356  Wuppertal     3          NaN
# Select only the 'Price' column for imputation
price_df = merged_df[['Price']]

# imp = SimpleImputer(missing_values=NaN, strategy='median')
# imputed_prices = imp.fit_transform(price_df)

# merged_df['Imputed Price'] = imputed_prices

# print(merged_df)
# merged_df.to_csv('cityImputRental.csv', index=False)

#median and mean gives us values like this so it might not be good so im going to try KNN or KmeanImputer
#           Name  Beds        Price  Imputed Price
# 0       Aachen     1  1622.333333    1622.333333
# 1       Aachen     2          NaN    1663.875000
# 2       Aachen     3  2109.500000    2109.500000
# 3       Aachen     4          NaN    1663.875000
# 4       Aachen     5          NaN    1663.875000
# ..         ...   ...          ...            ...
# 355  Wuppertal     2  1807.666667    1807.666667
# 356  Wuppertal     3          NaN    1663.875000
# 357  Wuppertal     4          NaN    1663.875000
# 358  Wuppertal     5          NaN    1663.875000
# 359  Wuppertal     6          NaN    1663.875000
imputer = KNNImputer(n_neighbors=3, weights="distance")
imputed_prices = imputer.fit_transform(price_df)
merged_df['Imputed Price'] = imputed_prices
print(merged_df)
merged_df.to_csv('cityImputRental.csv', index=False)
german_cities_by_state = {
    'Berlin': ['Berlin'],
    'Baden-Württemberg': ['Stuttgart', 'Mannheim', 'Karlsruhe', 'Freiburg im Breisgau', 'Heidelberg', 'Ulm', 'Pforzheim', 'Reutlingen', 'Esslingen', 'Ludwigsburg', 'Ostfildern', 'Kornwestheim', 'Weingarten', 'Eppelheim', 'Asperg'],
    'Bavaria': ['Munich', 'Nuremberg', 'Augsburg', 'Regensburg', 'Ingolstadt', 'Fürth', 'Würzburg', 'Erlangen', 'Rosenheim', 'Germering', 'Ottobrunn', 'Puchheim', 'Gröbenzell', 'Haar', 'Neubiberg'],
    'Hamburg': ['Hamburg'],
    'North Rhine-Westphalia': ['Cologne', 'Düsseldorf', 'Dortmund', 'Essen', 'Duisburg', 'Bochum', 'Wuppertal', 'Bielefeld', 'Bonn', 'Münster', 'Mönchengladbach', 'Gelsenkirchen', 'Aachen', 'Krefeld', 'Oberhausen', 'Hagen', 'Hamm', 'Mülheim', 'Leverkusen', 'Solingen', 'Herne', 'Neuss', 'Paderborn', 'Bottrop', 'Moers', 'Siegen', 'Gladbeck', 'Herten', 'Hilden', 'Siegburg', 'Eilendorf'],
    'Hesse': ['Frankfurt', 'Wiesbaden', 'Darmstadt', 'Kassel', 'Hattersheim', 'Obertshausen', 'Bad Soden am Taunus', 'Eschborn'],
    'Saxony': ['Leipzig', 'Dresden', 'Chemnitz', 'Halle'],
    'Lower Saxony': ['Hannover', 'Braunschweig', 'Oldenburg', 'Osnabrück', 'Wolfsburg', 'Göttingen', 'Salzgitter', 'Hildesheim'],
    'Rhineland-Palatinate': ['Mainz', 'Ludwigshafen', 'Koblenz', 'Trier', 'Kaiserslautern'],
    'Schleswig-Holstein': ['Kiel', 'Lübeck', 'Elmshorn', 'Pinneberg', 'Wentorf bei Hamburg', 'Schenefeld', 'Glinde'],
    'Bremen': ['Bremen'],
    'Saxony-Anhalt': ['Magdeburg', 'Halle', 'Halle-Neustadt'],
    'Thuringia': ['Erfurt', 'Jena'],
    'Mecklenburg-Vorpommern': ['Rostock', 'Schwerin'],
    'Saarland': ['Saarbrücken'],
    'Brandenburg': ['Potsdam'],
    'Rhineland-Palatinate': ['Kaiserslautern', 'Mainz', 'Ludwigshafen', 'Koblenz', 'Trier'],
}
#this function convert city to state
def get_state(city_name):
    for state, cities in german_cities_by_state.items():
        if city_name in cities:
            return state
    return None
result_df = merged_df.copy()
result_df['State'] = result_df.Name.apply(get_state)
result_df = result_df.groupby(by=['State','Beds'])['Imputed Price'].mean().reset_index()
print(result_df.head())
result_df.to_csv('stateRental.csv', index=False)
