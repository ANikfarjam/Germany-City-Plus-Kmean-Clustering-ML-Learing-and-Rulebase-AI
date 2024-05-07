#Author: Ashkan Nikfarjam, Ryan Fernald
#Using federal Arbeitsagentur (Employement Agency) data to extract information about available jobs in Germany
#source: https://rapidapi.com/relu-consultancy-relu-consultancy-default/api/arbeitsagentur-employement-agency/

import requests
import pandas as pd
from googletrans import Translator

"""
    example:
    url = "https://arbeitsagentur-employement-agency.p.rapidapi.com/search"

    querystring = {"token":"GANCDTjzQY","keyword":"python","location":"berlin","radius":"10"}

    headers = {
        "X-RapidAPI-Key": "5847527b5bmshe2f2f4e69370c30p1a3ec9jsn659fda58c155",
        "X-RapidAPI-Host": "arbeitsagentur-employement-agency.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

"""


# this api quarying data based on these keys
# keyword --> job title 
# location --->city 

# I ask Open API Caht GPT to catagorize jobs by industry and return a dictionary to me 

#now i can use this plus our cities df to get more jobs data i might adjust values for better result
def quary_job(job_keyword, city):
    url = "https://arbeitsagentur-employement-agency.p.rapidapi.com/search"
    querystring = {"token": "GANCDTjzQY", "keyword": job_keyword, "location": city, "radius": "10"}
    headers = {
        "X-RapidAPI-Key": "5847527b5bmshe2f2f4e69370c30p1a3ec9jsn659fda58c155",
        "X-RapidAPI-Host": "arbeitsagentur-employement-agency.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    translator = Translator()

    city = []  # ort
    title = []  # titel
    external_link = []  # 'externeUrl'

    for job in response.json()['data']:
        city.append(job['ort'])
        # Translate the title from German to English
        translated_title = translator.translate(job['titel'], src='de', dest='en').text
        title.append(translated_title)
        external_link.append(job['externeUrl'])

    return city, title, external_link