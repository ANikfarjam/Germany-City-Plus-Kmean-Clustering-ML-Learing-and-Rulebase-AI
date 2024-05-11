#Author: Ashkan Nikfarjam
#this is our recommendation Enging
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os
import joblib
import numpy as np


def recommend(user_array=None):
    #[(['work', 'study'], 'alone', 1, 1234444, 44444444, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ['Protestant'])]
#     element_ids = [
#     "purpose-checklist" -> work/study/mariage/emigration
#     "num-people-dropdown",->alone
#     "num-people-slider", ->number of price
#     "min-price",
#     "max-price",
#     "education-pref-slider",
#     "jobs-pref-slider",
#     "income-pref-slider",
#     "safety-pref-slider",
#     "health-pref-slider",
#     "environment-pref-slider",
#     "civic-engagement-pref-slider",
#     "accessibility-pref-slider",
#     "housing-pref-slider",
#     "community-pref-slider",
#     "life-satisfaction-pref-slider",
#     "religious-preferences"
# ]
    print(user_array[0][5:16])
    # Load the model
    kmeans_model = joblib.load('./Recomendation/kmeans_model.pkl')
    # Extract columns 6 to 15
    user = user_array[0][5:16]
    # Reshape the user data to a 2D array
    scaler = StandardScaler()
    scaled_user = scaler.fit_transform(np.array(user).reshape(1, -1))
    clustered_user =  kmeans_model.predict(scaled_user)
    ########
    #For recomendation I am implementing a combination rule based and learning agent
    #rule based agent is type agent that works based on semantic network
    #it makes infrances and decission based on if() then()
    #unlike ligic base agent that uses logical inferances
    #the world represenation is an array
    #for searchability we just sort our pandas
    clustered_states_df = pd.read_csv('./Training/clustered_recomend.csv')
    #first rulebase infrance
    assert(clustered_user >=0)
    qualified_States = clustered_states_df[clustered_states_df['Cluster']==clustered_user[0]]
    qualified_States_lst = qualified_States.Region.to_list()
    
    cities_list = []
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
    for states in qualified_States_lst:
        if states in german_cities_by_state:
            cities_list.append(german_cities_by_state[states])
    # for state, cities in german_cities_by_state:
    #     for rigions in qualified_States_lst:
    #         if rigions == state:
    #             cities_list.append(cities)
    
    #2nd infrance about appartments
    #here if user chose work if so they can do work recomendation

    #3rd inrfrance
    #rental 
    rental_df = pd.read_csv('./DATA/Rentals/cityImputRental.csv')
    numPPl = 1
    if user_array[0][2] > 1:
        if user_array[0][3]: #Search for the berdrooms number preferances
            minbound = user_array[0][3] - 1
            maxbound = user_array[0][3] + 1
            rental_df = rental_df[(rental_df.Name.isin(cities_list)) & (rental_df.Beds >= minbound) & (rental_df.Beds <= maxbound)]
        else:
            rental_df = rental_df[((rental_df.Name.isin(cities_list)) & rental_df.Beds == numPPl)]
        #4th infrance 
        #rental with price range
        if user_array[0][4] or user_array[0][5]:
            if user_array[0][5]:
                rental_df = rental_df[(rental_df['Imputed Price'] >= user_array[0][4]) & (rental_df.Beds <= user_array[0][5])]
            else:
                rental_df = rental_df[(rental_df['Imputed Price'] >= user_array[0][4])]
    #Wrold adjustment
    #result_citie = rental_df.Name.to_list()
    
    return rental_df, qualified_States
    
#print(recommend([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#print(recommend(list([(['work', 'study'], 'alone', 1, 1234444, 44444444, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ['Protestant'])])))
#print(type(form_responses)) 
