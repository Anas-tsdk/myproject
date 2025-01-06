from dash import html, dcc
from src.components.component1 import afficher_map
from dash.dependencies import Input, Output
from dash import html, dcc

def simple_page():
    """
    Crée et retourne la mise en page pour la page 'simple_page',
    incluant la carte générée par Folium et un bouton pour choisir la colonne.
    """

    # Retourne la structure HTML de la page avec un bouton radio
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.H1("Carte du Monde", style={"textAlign": "center", "marginBottom": "20px"}),  # Titre
                    html.Div(id="carte-container"),  # Conteneur de la carte, mis à jour dynamiquement
                ],
                style={"padding": "20px"}
            ),
            
            # Ajouter un bouton radio pour choisir la colonne à afficher sur la carte
            dcc.RadioItems(
                id='data-toggle',
                options=[
                    {'label': 'Total Affected', 'value': 'Total Affected'},
                    {'label': 'Total Damage', 'value': 'Total Damage, Adjusted (\'000 US$)'},
                    {'label': 'Appeal', 'value': 'Appeal'}
                ],
                value='Total Affected',  # Valeur par défaut
                labelStyle={'display': 'inline-block'}
            )
        ]
    )