#author: Ashkan Nikfarjam
import pandas as pd
import plotly.express as px

age_employee = pd.read_csv("empl_age.csv")

ageEMP_graph = px.bar(age_employee, x='age group', y='count', animation_frame='year')

ageEMP_graph.update_layout(title='Employement by Age Group Over Time')
ageEMP_graph.show()