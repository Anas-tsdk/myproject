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

if __name__ == "__main__":
    # Créer l'application Dash
    app = dash.Dash(__name__)

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
            footer()  # Ajouter le footer en bas de la page
        ],
        style={
            'display': 'flex',
            'flexDirection': 'column',  # Organise les éléments en colonne
            'minHeight': '100vh',  # Occupe toute la hauteur de la fenêtre du navigateur
            'height': '100%',  # Assurez-vous que le conteneur parent occupe bien toute la hauteur
            'justifyContent': 'space-between'  # Cela force le footer à se placer en bas
        }
    )

     # Callback pour afficher le contenu en fonction de l'URL
    @app.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]
    )
    def update_page(pathname):
        if pathname == "/stats":  # Page "Graphes"
            return simple_page()
        elif pathname == "/about":  # Page "À propos"
            return about_page()
        else:  # Par défaut, page d'accueil
            return home_page()

    # Lancer l'application Dash
    app.run_server(debug=True, port=8051)
