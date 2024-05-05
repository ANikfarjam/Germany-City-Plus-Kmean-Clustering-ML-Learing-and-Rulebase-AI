import dash_bootstrap_components as dbc
from dash import html


history_card = dbc.Card(
    [
        dbc.CardImg(src="assets/history.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Postwar History", className="histoy_card"),
                html.P(
                    "Learn about how wars in Germany effected the landscape in modern day",
                    className="card-text",
                ),
                dbc.Button("Read", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)
questionare_card = dbc.Card(
    [
        dbc.CardImg(src="assets/question.png", top=True),
        dbc.CardBody(
            [
                html.H4("City Recomendation", className="recomend_card"),
                html.P(
                    "Our implemented AI is able to recommend a city tailored to your need.",
                    "We rocemmend you to fill up these questions to start",
                    className="card-text",
                ),
                dbc.Button("Start", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)