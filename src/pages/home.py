from dash import html
from src.components.component2 import afficher_histogramme  

def home_page():
    return html.Div(
        children=[
            html.H1("Bienvenue sur la page d'accueil", style={"textAlign": "center"}),
            html.P("Ceci est la page d'accueil de l'application."),
            afficher_histogramme()  # Utilisation du composant
        ],
        style={"padding": "20px"}
    ) 
