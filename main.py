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
from src.components.component1 import afficher_map
from src.components.component2 import afficher_histogramme
import importlib
import subprocess
import sys
import webbrowser
import threading
import time
from config import (
    PAGE_CONTENT_STYLE,
    APP_LAYOUT_STYLE,
    ROUTES,
    BROWSER_DELAY,
    APP_URL,
    APP_PORT,
    APP_DEBUG,
)


def install_requirements():
    """Vérifie et installe les dépendances manquantes"""
    print("Vérification des dépendances...")
    try:
        with open("requirements.txt") as f:
            required = {}
            for line in f:
                if "==" in line:
                    package, version = line.strip().split("==")
                    required[package] = version

        for package, version in required.items():
            try:
                importlib.import_module(package)
            except ImportError:
                print(f"Installation de {package}...")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", f"{package}=={version}"]
                )
    except FileNotFoundError:
        print("Erreur: Le fichier requirements.txt n'a pas été trouvé.")
        sys.exit(1)


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
            html.Div(id="page-content", style=PAGE_CONTENT_STYLE),
            footer(),
        ],  # Ajouter le footer en bas de la page
        style=APP_LAYOUT_STYLE,
    )

    # Callback combiné pour afficher le contenu de la page et la carte
    @app.callback(
        Output("page-content", "children"),
        [
            Input("url", "pathname")
        ],  # Vous n'avez plus besoin d'Input pour le bouton radio ici
    )
    def update_page_and_map(pathname):
        """
        Met à jour le contenu de la page selon l'URL.

        Args:
        pathname (str): Chemin de l'URL

         Returns:
        html.Div: Contenu de la page correspondante
        """
        # Logique pour le contenu de la page
        if pathname == ROUTES["STATS"]:
            return simple_page()
        elif pathname == ROUTES["ABOUT"]:
            return about_page()
        elif pathname in ROUTES["HOME"]:
            return home_page()

    # Callback pour mettre à jour la carte en fonction de la colonne sélectionnée
    @app.callback(
        Output("carte-container", "children"),
        [Input("data-toggle", "value")],  # Prendre la valeur du bouton radio
    )
    def update_map(colonne):
        """
        Met à jour la carte selon la colonne sélectionnée.

        Args:
        colonne (str): Nom de la colonne à afficher

        Returns:
        html.Div: Carte mise à jour
        """

        # Affiche la carte avec la colonne choisie
        return afficher_map(colonne)

    @app.callback(
        Output("histogram-container", "children"),
        [Input("date-slider", "value")],  # Valeur du curseur
    )
    def update_histogram(value):
        """
         Met à jour l'histogramme selon la période sélectionnée.

         Args:
        value (list): [année_début, année_fin]

         Returns:
        html.Div: Histogramme mis à jour
        """

        (
            start_year,
            end_year,
        ) = value  # Dash fournit un seul argument sous la forme d'une liste
        # Met a jour avec les valeurs selectionnées
        return afficher_histogramme(start_year, end_year)

    def open_browser():
        """
        Ouvre le navigateur web vers l'application après un délai.
        """

    time.sleep(BROWSER_DELAY)
    webbrowser.open(APP_URL)
    # Lancer le navigateur
    threading.Timer(BROWSER_DELAY, open_browser).start()
    # Lancer l'application
    print("Lancement de l'application...")

    # Lancer l'application Dash
    app.run_server(debug=APP_DEBUG, port=APP_PORT)
