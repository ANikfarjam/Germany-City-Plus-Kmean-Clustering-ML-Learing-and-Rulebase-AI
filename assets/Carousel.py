import dash_bootstrap_components as dbc
from dash import html

history_carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/background-slides/2.png"},
        {"key": "2", "src": "/assets/background-slides/3.png"},
        {"key": "3", "src": "/assets/background-slides/4.png"},
        {"key": "4", "src": "/assets/background-slides/5.png"},
        {"key": "5", "src": "/assets/background-slides/6.png"},
        {"key": "6", "src": "/assets/background-slides/7.png"},
        {"key": "7", "src": "/assets/background-slides/8.png"},
        {"key": "8", "src": "/assets/background-slides/9.png"},
        {"key": "9", "src": "/assets/background-slides/10.png"},
        {"key": "10", "src": "/assets/background-slides/11.png"},
        {"key": "11", "src": "/assets/background-slides/12.png"},
        {"key": "12", "src": "/assets/background-slides/13.png"},
    ],
    controls=True,
    indicators=True,
    #close = True,
)

