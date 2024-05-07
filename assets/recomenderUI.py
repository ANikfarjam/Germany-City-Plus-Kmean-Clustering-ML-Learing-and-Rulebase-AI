from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

form_responses = []
# Form components
purpose = html.Div([
    dbc.Label("What is your purpose of moving?", html_for="purpose"),
    dcc.Checklist(
        id="purpose-checklist",
        options=[
            {"label": "Work", "value": 'work'},
            {"label": "Study", "value": 'study'},
            {"label": "Marriage", "value": 'marriage'},
            {"label": "Emigration", "value": 'emigration'},
        ],
        value=['work'],
    ),
], className="mb-3",)

num_people = html.Div(
    [
        dbc.Label("Are you moving alone or with family/friends/partner?", html_for="numppl"),
        dcc.Dropdown(
            id="num-people-dropdown",
            options=[
                {"label": "Alone", "value": "alone"},
                {"label": "Family/Others", "value": "family_others"},
            ],
            value="alone",
        ),
    ],
    className="mb-3",
)

np_slider = html.Div(
    [
        dbc.Label("If yes, how many people?", html_for="range-slider", id="num-people-label"),
        dcc.Slider(id="num-people-slider", min=0, max=10, step=1, value=1),
    ],
    id="num-people-slider-container",  
    className="mb-3",
)

# Rental Preferences
rentals = html.Div(
        [   
            dbc.Label("Rental Preferences:", html_for="range-slider", id="rental-label"),
            html.Div(
                [
                    dbc.Label("Min", width="auto"),
                    dbc.Col(
                        dbc.Input(id="min-price", type="number", placeholder="min price"),
                        className="me-3",
                    ),
                    dbc.Label("Max", width="auto"),
                    dbc.Col(
                        dbc.Input(id="max-price", type="number", placeholder="max price"),
                        className="me-3",
                    )
        ],)
        ],
        className="g-2",
)

# Preferences
#Education,Jobs,Income,Safety,Health,
#Environment,Civic engagement,Accessiblity to services,Housing,Community,Life satisfaction
preferences = html.Div(
    [ 
        dbc.Label("Please rate how important the following categories are to you.", id="preference-intro-label"),
        
        # Education
        html.Div([
            dbc.Label("Education:", id="preference-slider-education"),
            dcc.Slider(id="education-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Jobs
        html.Div([
            dbc.Label("Jobs:", id="preference-slider-jobs"),
            dcc.Slider(id="jobs-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Income
        html.Div([
            dbc.Label("Income:", id="preference-slider-income"),
            dcc.Slider(id="income-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Safety
        html.Div([
            dbc.Label("Safety:", id="preference-slider-safety"),
            dcc.Slider(id="safety-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Health
        html.Div([
            dbc.Label("Health:", id="preference-slider-health"),
            dcc.Slider(id="health-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Environment
        html.Div([
            dbc.Label("Environment:", id="preference-slider-environment"),
            dcc.Slider(id="environment-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Civic engagement
        html.Div([
            dbc.Label("Civic engagement:", id="preference-slider-civic-engagement"),
            dcc.Slider(id="civic-engagement-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Accessibility to services
        html.Div([
            dbc.Label("Accessibility to services:", id="preference-slider-accessibility"),
            dcc.Slider(id="accessibility-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Housing
        html.Div([
            dbc.Label("Housing:", id="preference-slider-housing"),
            dcc.Slider(id="housing-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Community
        html.Div([
            dbc.Label("Community:", id="preference-slider-community"),
            dcc.Slider(id="community-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
        
        # Life satisfaction
        html.Div([
            dbc.Label("Life satisfaction:", id="preference-slider-life-satisfaction"),
            dcc.Slider(id="life-satisfaction-pref-slider", min=0, max=10, step=0.5, value=2),
        ], className="mb-3"),
    ],
    id="preferences-slider-container",  
    className="mb-3",
)

submit_button = html.Button('Submit Form', id='submit-button',n_clicks=0)
next = dbc.Button("Next Step", href='/NextStep')

response_element = html.Div([
    f"{form_responses}",
    html.Div(id="form-responses")  # Display form responses
])

form = dbc.Form([purpose, num_people, np_slider, rentals, preferences, submit_button, response_element,next],style={'padding': '50px 48px'})





