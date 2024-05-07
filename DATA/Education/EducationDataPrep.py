#author: Ashkan Nikfarjam  
from operator import index
import pandas as pd
public_schools = pd.read_csv('matchedCitySchools.csv')
public_schools.rename(columns={'Number of schools':'Number of public schools'}, inplace=True)
print(public_schools.head())
int_schools = pd.read_csv('intSchootranking.csv')
print(int_schools.head())
city = pd.read_csv('../German cities.csv')
city = city[['city']]
print(city.head())
unv_df = pd.read_csv('unvercities.csv')
unv_df = unv_df.city.value_counts().reset_index()
unv_df.rename(columns={'count':'Number of univercities'}, inplace=True)
print(unv_df.head())
merged_df = pd.merge(city, public_schools, on='city', how='left')
merged_df.fillna(0, inplace=True)
merged_df = pd.merge(merged_df, int_schools, on='city', how='left')
merged_df.fillna(0, inplace=True)
merged_df = pd.merge(merged_df, unv_df, on='city', how='left')
merged_df.fillna(0, inplace=True)
print(merged_df.head())
merged_df.drop(columns='Rating', inplace=True)
merged_df['total']=merged_df['Number of public schools'] + merged_df['Number of international schools'] + merged_df['Number of univercities']
print(merged_df.head())
merged_df.to_csv('cityTotalSchools.csv', index=False)
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
merged_df['State'] = merged_df.city.apply(get_state)
state_df = merged_df.copy().drop(columns='city')
state_df = state_df.groupby(by='State').sum().reset_index()
print(state_df.head())
state_df.to_csv('stateTotalSchools.csv', index=False)
