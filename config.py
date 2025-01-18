# Configuration de l'application

APP_PORT = 8051
APP_HOST = "127.0.0.1"
APP_DEBUG = False
APP_URL = f"http://{APP_HOST}:{APP_PORT}/"

# Chemin du fichier
DATA_FILE = "data/cleaned/cleaned_data.csv"

# Style global de l'application
APP_LAYOUT_STYLE = {
    "display": "flex",
    "flexDirection": "column",
    "minHeight": "100vh",
    "height": "100%",
    "justifyContent": "space-between",
}

# Style du conteneur de page
PAGE_CONTENT_STYLE = {"flexGrow": 1, "padding": "20px"}

# Routes de l'application
ROUTES = {"HOME": ["/", "/home"], "STATS": "/stats", "ABOUT": "/about"}

# Délai pour l'ouverture du navigateur (en secondes)
BROWSER_DELAY = 1.5
