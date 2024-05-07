#this is propaply going to be ignored
import json
import pandas as pd
from googletrans import Translator


with open('extractedjobs.json', 'r') as file:
    data = json.load(file)
#keys in json file
#slug
#company_name
#title
#description
#remote
#url
#tags
#job_types
#location
#created_at

job_position = []
company = []
job_title = []
is_remote = []
location =[]

for job in data['data']:
    job_position.append(job['slug'])
    company.append(job['company_name']) 
    job_title.append(job['title']) 
    is_remote.append(job['remote']) 
    location.append(job['location'])
    

print(location[:3])

employment_df = pd.DataFrame({'city':location, 
                              'company': company,
                              'JobTitle':job_title,
                              'isRemot':is_remote
                              }
                              )

#now the data is ready we can translate them
def translate_text(text, target_language='en'):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_language)
        return translated_text.text
    except Exception as e:
        print("Error translating:", e)
        return "Translation Error"
print(employment_df.columns)
print("translating please wait!")
for column in employment_df.columns:
    employment_df[str(column)].apply(translate_text)
employment_df.to_csv('resultEmployment.csv', index=False)