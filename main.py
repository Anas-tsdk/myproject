from src.utils.get_data import get_data
from src.utils.clean_data import clean_data
from dash.dependencies import Input, Output
import dash
from dash import dcc, html
from src.components.footer import footer
from src.components.header import header
from src.components.navbar import navbar 
from src.pages.simple_page import simple_page
from src.pages.home import home_page
from src.pages.about import about_page
from src.components.component1 import afficher_map  # Assurez-vous d'importer cette fonction
from src.components.component2 import afficher_histogramme

if __name__ == "__main__":
    # Créer l'application Dash avec suppress_callback_exceptions=True
    app = dash.Dash(__name__, suppress_callback_exceptions=True)

    # Appeler get_data() et clean_data() une seule fois
    data = get_data()   
    clean_data(data)

    # Layout de l'application Dash
    app.layout = html.Div(
        children=[
            dcc.Location(id="url", refresh=False),  # Permet de capturer l'URL
            navbar,  # Ne pas appeler navbar() mais utiliser navbar directement
            header(),  # Ajouter le header en haut de la page
            html.Div(id="page-content", style={"flexGrow": 1, "padding": "20px"}),  # Contenu des pages
            footer()
        ],  # Ajouter le footer en bas de la page
        style={
            'display': 'flex',
            'flexDirection': 'column',  # Organise les éléments en colonne
            'minHeight': '100vh',  # Occupe toute la hauteur de la fenêtre du navigateur
            'height': '100%',  # Assurez-vous que le conteneur parent occupe bien toute la hauteur
            'justifyContent': 'space-between'  # Cela force le footer à se placer en bas
        }
    )

    # Callback combiné pour afficher le contenu de la page et la carte
    @app.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]  # Vous n'avez plus besoin d'Input pour le bouton radio ici
    )
    def update_page_and_map(pathname):
        # Logique pour le contenu de la page
        if pathname == "/stats":  # Page "Graphes"
            return simple_page()  # La page simple ne dépend plus du "colonne"
        elif pathname == "/about":  # Page "À propos"
            return about_page()
        elif pathname == "/home":
            return home_page()

    # Callback pour mettre à jour la carte en fonction de la colonne sélectionnée
    @app.callback(
        Output("carte-container", "children"),
        [Input('data-toggle', 'value')]  # Prendre la valeur du bouton radio
    )
    def update_map(colonne):
        # Affiche la carte avec la colonne choisie
        return afficher_map(colonne)
    
    @app.callback(
    Output("histogram-container", "children"),  
    [Input("date-slider", "value")]  # Valeur du curseur
)
    def update_histogram(value ): 
        
        start_year, end_year = value # Dash fournit un seul argument sous la forme d'une liste
        # met a jour avce les valeurs selectionnées 
        return afficher_histogramme(start_year, end_year)

    # Lancer l'application Dash
    app.run_server(debug=True, port=8051)
