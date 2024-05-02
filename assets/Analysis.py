#Author: Ashkan Nikfarjam
import plotly.express as px
import pandas as pd

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
city_df = pd.read_csv("./DATA/German cities.csv")
#creating Rentals df for map
rental = pd.read_csv("./DATA/Rentals/cityRentals.csv")
rental.Price = rental.Price.astype(int)
rental  = rental.groupby(by=['Name','Beds']).Price.mean().reset_index()
#print(rental)
rental_pd = pd.DataFrame(rental).reset_index()
# Merge DataFrames on the 'city' column
rental_df = pd.merge(rental, city_df.copy(), how='left', left_on='Name', right_on='city')

# Drop the redundant 'city' column
rental_df.drop(columns=['city'], inplace=True)
rental_df = rental_df.rename({'Price':'Average Price'})
#print(rental_df.head())
#creating healthcare data frame for the map
HealthCare_data = pd.read_csv("./DATA/Helthcare/numberofHospitals.csv")
HealthCare_data.rename(columns={'City':'city'}, inplace=True)
healthCare_df = pd.merge(city_df.copy(), HealthCare_data, on='city')

#schools
school = pd.read_csv("./DATA/Education/matchedCitySchools.csv")
school_df = pd.merge(school, city_df.copy(), on='city', how='left')
# environment
environment = pd.read_csv("./DATA/Environment/temperature_by_state.csv")
weather = pd.read_csv("./DATA/Environment/weather.csv")

# public transportation 
public_transportation = pd.read_csv("./DATA/Public Transportation/transportation.csv")
# # politics
# politics = pd.read_csv("./DATA/Politics/politics.csv")
print(public_transportation)



#print(school_df.head())
#use this df for city population
mod_city = city_df.copy()
mod_city = mod_city.dropna()

#number of Pharmecy
pharmacy = pd.read_csv('./DATA/Helthcare/numberOfPharmecies.csv')

#rint("pharmecy", pharmacy.head())
#print(city_df.head())
pharmacy_df = pd.merge(pharmacy, city_df.copy() , on='city', how='left')
print(pharmacy_df.head())
