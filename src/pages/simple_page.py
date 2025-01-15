from dash import html, dcc
from src.components.component1 import afficher_map
from src.components.component4 import affiche_nuages
from src.components.component3 import afficher_camembert
from dash.dependencies import Input, Output
from dash import html, dcc

def simple_page():
    """
    Crée et retourne la mise en page pour la page 'simple_page',
    incluant la carte générée par Folium et un bouton pour choisir la colonne, on y ajoute aussi un camembert sur les 3 grand groupes de catastrophes .
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
                    {'label': 'Classification Key', 'value': 'Classification Key'}
                ],
                value='Total Affected',  # Valeur par défaut
                labelStyle={'display': 'inline-block'}
            ),
            # Section pour le graphique camembert
            html.Div(
                children=[
                    html.H1("Répartition des Types de Catastrophes", style={"textAlign": "center", "marginTop": "50px"}),  # Titre
                    afficher_camembert()  # Afficher le graphique camembert
                ],
                style={"padding": "20px"}
            ),

            # Section pour le graphique camembert
            html.Div(
                children=[
                    html.H1("Répartition aides", style={"textAlign": "center", "marginTop": "50px"}),  # Titre
                    affiche_nuages()  # Afficher le graphique camembert
                ],
                style={"padding": "20px"}
            ),
        ]
    )
     