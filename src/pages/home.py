from dash import html

def home_page():
    return html.Div(
        children=[
            html.H1("Bienvenue sur la page d'accueil", style={"textAlign": "center"}),
            html.P("Ceci est la page d'accueil de l'application."),
        ],
        style={"padding": "20px"}
    )
