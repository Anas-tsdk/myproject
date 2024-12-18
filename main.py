from src.utils.get_data import get_data
from src.utils.clean_data import clean_data
import dash
from dash import dcc, html
from src.components.footer import footer

if __name__ == "__main__":
    
    # Créer l'application Dash
    app = dash.Dash(__name__)

    # Appeler get_data() et clean_data() une seule fois
    data = get_data()   
    clean_data(data)

    # Layout de l'application Dash
    app.layout = html.Div(children=[
        html.H1("Tempêtes et Santé Publique"),  # Ajouter un titre
        #footer()  # Appel du footer
    ])

    # RUN APP
    app.run_server(debug=True, port = 8051)