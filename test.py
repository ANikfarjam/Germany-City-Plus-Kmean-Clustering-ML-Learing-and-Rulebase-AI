from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Define an empty list to store form responses
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
        dcc.Slider(id="num-people-slider", min=0, max=10, step=1, value=2),
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
preferences = html.Div(
    [
        dbc.Label("Please rate how important the following categories are to you.", id="preference-intro-label"),
        html.Div([
            # Environment
            dbc.Label("Environment:", id="preference-slider-environment"),
            dcc.Slider(id="environment-pref-slider", min=0, max=10, step=1, value=2),
        ], className="mb-3"),
        html.Div([
            # Civic engagement
            dbc.Label("Civic engagement:", id="preference-slider-civic-engagement"),
            dcc.Slider(id="civic-engagement-pref-slider", min=0, max=10, step=1, value=2),
        ], className="mb-3"),
        html.Div([
            # Safety
            dbc.Label("Safety:", id="preference-slider-safety"),
            dcc.Slider(id="safety-pref-slider", min=0, max=10, step=1, value=2),
        ], className="mb-3"),
        html.Div([
            # Community
            dbc.Label("Community:", id="preference-slider-community"),
            dcc.Slider(id="community-pref-slider", min=0, max=10, step=1, value=2),
        ], className="mb-3"),
        html.Div([
            # Life satisfaction
            dbc.Label("Life satisfaction:", id="preference-slider-life-satisfaction"),
            dcc.Slider(id="life-satisfaction-pref-slider", min=0, max=10, step=1, value=2),
        ], className="mb-3"),
        html.Div([
            # Religious preferences
            dbc.Label("Religious preferences:", id="preference-slider-religious-preferences"),
            dcc.Checklist(
                id="religious-preferences",
                options=[
                    {"label": "Protestant", "value": 'Protestant'},
                    {"label": "Catholic", "value": 'Catholic'},
                    {"label": "Non-religious", "value": 'Non-religious'},
                    {"label": "Other", "value": 'Other'},
                    {"label": "Doesn't matter", "value": 'NA'},
                ],
                value=['Protestant'],
            ),
        ], className="mb-3"),
    ],
    id="preferences-slider-container",
    className="mb-3",
)

submit_button = html.Button('Submit Form', id='submit-button', n_clicks=0)

form = dbc.Form([purpose, num_people, np_slider, rentals, preferences, submit_button])

# Layout
app.layout = html.Div([
    dcc.Location(id="url"),
    form,
    html.Div(id="form-responses")  # Display form responses
])

# Callbacks to update form responses list
@app.callback(
    Output("num-people-slider-container", "style"),
    [Input("num-people-dropdown", "value")]
)
def update_num_people_visibility(purpose_value):
    if purpose_value == "family_others":  # Only show slider if "Family/Others" is selected
        return {"display": "block"}
    else:
        return {"display": "none"}

@app.callback(
    Output("num-people-label", "children"),
    [Input("num-people-dropdown", "value")]
)
def update_num_people_label(value):
    if value == "family_others":
        return "If yes, how many people?"
    else:
        return "If yes, how many family members/others?"

# Callback to update form responses list when the submit button is clicked
@app.callback(
    Output("form-responses", "children"),
    [Input("submit-button", "n_clicks")],
    [State(component_id, "value") for component_id in ["purpose-checklist", "num-people-dropdown", "num-people-slider", "min-price", "max-price", "environment-pref-slider", "civic-engagement-pref-slider", "safety-pref-slider", "community-pref-slider", "life-satisfaction-pref-slider", "religious-preferences"]]
)
def update_form_responses(n_clicks, *args):
    if n_clicks > 0:
        form_responses.append(args)
        print(form_responses)  # Print form responses
        return f"Form submitted. Responses: {form_responses}"
    else:
        return ""

if __name__ == '__main__':
    app.run_server(debug=True)
