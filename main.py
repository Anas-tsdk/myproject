from src.utils.get_data import get_data
from src.utils.clean_data import clean_data
import dash
from dash import dcc, html
from src.components.footer import footer
from src.components.header import header
from src.components.navbar import navbar  # Importez correctement la navbar

if __name__ == "__main__":
    # Créer l'application Dash
    app = dash.Dash(__name__)

    # Appeler get_data() et clean_data() une seule fois
    data = get_data()   
    clean_data(data)

    # Layout de l'application Dash
    app.layout = html.Div(
        children=[
            navbar,  # Ne pas appeler navbar() mais utiliser navbar directement
            header(),  # Ajouter le header en haut de la page
            html.Div(
                style={'flexGrow': 1, 'padding': '20px'}  # Ce div occupe l'espace restant et permet de pousser le footer en bas
            ),
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

    # Lancer l'application Dash
    app.run_server(debug=True, port=8051)
