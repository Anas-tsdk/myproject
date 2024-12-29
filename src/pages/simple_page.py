from dash import html
from src.components.component1 import afficher_map

def simple_page(colonne):
    """
    Crée et retourne la mise en page pour la page 'simple_page',
    incluant la carte générée par Folium.
    """
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.H1("Carte du Monde", style={"textAlign": "center", "marginBottom": "20px"}),  # Titre
                    afficher_map(colonne)  # Intégration de la carte avec la colonne choisie
                ],
                style={"padding": "20px"}
            )
        ]
    )
