from dash import html
from src.components.navbar import navbar
from src.components.header import header
from src.components.footer import footer
from src.components.component1 import afficher_map

def simple_page():
    """
    Crée et retourne la mise en page pour la page 'simple_page',
    incluant la carte générée par Folium.
    """
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.H1("Carte du Monde", style={"textAlign": "center", "marginBottom": "20px"}),  # Titre
                    afficher_map()  # Intégration de la carte
                ],
                style={"padding": "20px"}
            )
        ]
    )
