#Author: Ashkan Nikfarjam
#this is our recommendation Enging
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os
import joblib
import numpy as np
from assets.recomenderUI import form_responses

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
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    # Construct the full path to kmeans_model.pkl
    model_path = os.path.join(script_dir, 'kmeans_model.pkl')
    # Load the model
    kmeans_model = joblib.load(model_path)
    # Extract columns 6 to 15
    user = user_array[0][5:16]
    # Reshape the user data to a 2D array
    scaler = StandardScaler()
    scaled_user = scaler.fit_transform(np.array(user).reshape(1, -1))
    return kmeans_model.predict(scaled_user)

#print(recommend([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
print(recommend(list([(['work', 'study'], 'alone', 1, 1234444, 44444444, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ['Protestant'])])))
#print(type(form_responses)) 