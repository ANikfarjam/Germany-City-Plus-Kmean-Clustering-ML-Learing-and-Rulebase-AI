#Author: Ashkan Nikfarjam
#this is our recommendation Engine

import pandas as pd
import sys
import os

# Assuming this script is inside a package, make sure the parent directory is included in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import Train module from Training package
from Training import Train
from assets.recomenderUI import form_responses

def recommend(user_array=None):
    # Load user data
    user = user_array[0][2:13]
    
    # Predict using the kmeans model from Train module
    return Train.kmeans.predict(user)

recommend([(['work', 'study'], 'alone', 1, 1234444, 44444444, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ['Protestant'])])
