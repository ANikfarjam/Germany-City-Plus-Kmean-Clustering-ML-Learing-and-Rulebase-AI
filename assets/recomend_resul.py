from matplotlib import container
from Recomendation.RecommendEngine import recommend
import pandas as pd
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
#from assets.recomenderUI import form_responses
def initialize(fform_responses):
    return recommend(fform_responses)
#card function 
def create_card(state, form_responses):
    [_, world_df] = list(initialize(form_responses))
    copy_df = world_df.copy()
    copy_df.set_index('Region', inplace=True)
    # print(copy_df)
    card = dbc.Card(
        [
            dbc.CardHeader(state),
            dbc.CardBody(
                [
                    html.H4("Statistics:", className="recomend_card"),
                    dcc.Markdown(
                        "Average Education Rating: " + str(copy_df.loc[state, 'Education']) + "<br>" +
                        "Average Jobs Rating: " + str(copy_df.loc[state, 'Jobs']) + "<br>" +
                        "Average Income Rating: " + str(copy_df.loc[state, 'Income']) + "<br>" +
                        "Average Safety Rating: " + str(copy_df.loc[state, 'Safety']),
                        dangerously_allow_html=True
                    ),
                ]
            ),
        ],
        style={"width": "18rem"},
    )
    return card
#recomnedation container
def create_container(form_responses):
    [city_df, States] = list(recommend(form_responses))
    container_r = html.Div([
        html.Div([create_card(state,form_responses) for state in States.Region.to_list()]),
        city_table(city_df),
    ], style={'display': 'flex'})
    print("FINISHED CREATING")
    #cards = [create_card(state,form_responses) for state in States.Region.to_list()]
    #table = city_table(city_df)
    return container_r

def city_table(df):
    cp_df = df.copy()
    cp_df.drop(columns='Price', inplace=True)
    cp_df.rename(columns={'Name': 'city'}, inplace=True)
    cities_education = pd.read_csv('./DATA/Education/cityTotalSchools.csv')
    health = pd.read_csv('./DATA/Helthcare/numberofHospitals.csv')
    health2 = pd.read_csv('./DATA/Helthcare/numberOfPharmecies.csv')

    merge_df = pd.merge(cp_df, cities_education, on='city', how='left').reset_index()
    merge_df = pd.merge(merge_df, health, on='city', how='left').reset_index()
    #merge_df = pd.merge(merge_df, health2, on='city', how='left').reset_index()

    merge_df.fillna(0, inplace=True)
    
    print(merge_df)
    
    # Drop the existing index without inserting it as a new column
   

    
    return dbc.Table.from_dataframe(merge_df, striped=True)


#work
wordForm = 1