from dash import html,dcc
from src.components.component2 import afficher_histogramme  

def home_page():
    return html.Div(
        children=[

            html.H1("Bienvenue sur la page d'accueil", style={"textAlign": "center"}),
            html.P("Ceci est la page d'accueil de l'application."),

            # Ajoute un curseur pour sélectionner l'intervalle de dates
            html.Div([
                html.Label("Selectionnez l'intervalle d'annees:"),
                dcc.RangeSlider(
                    id="date-slider", 
                    min=2000, 
                    max=2025,  # ajustez en fonction des données réelles
                    step=1,
                    marks={i: str(i) for i in range(2000, 2024, 1)},  # Marquer les années tous les 1 ans
                    value=[2000, 2023]  # Valeur initiale 
                )
            ], style={"marginBottom": "20px"}),

            # Le composant graphique qui sera mis à jour
            html.Div(id="histogram-container"),
        ],
        style={"padding": "20px"}
    ) 