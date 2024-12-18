import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Créer l'application Dash
app = dash.Dash(__name__)
app.title = "Dashboard avec Navbar"

# Structure de la barre de navigation
navbar = html.Div(
    [
        html.Ul(
            [
                html.Li(html.A("Accueil", href="/", className="nav-link"), className="nav-item"),
                html.Li(html.A("Graphes", href="/stats", className="nav-link"), className="nav-item"),
                html.Li(html.A("À propos", href="/about", className="nav-link"), className="nav-item"),
            ],
            className="navbar",
        )
    ],
    className="navbar-container"
)

# Pages du dashboard
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),  # Permet la navigation entre les pages
        navbar,
        html.Div(id="page-content"),  # Conteneur pour le contenu de chaque page
    ]
)

# Callbacks pour le contenu de chaque page
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/":
        return html.Div(
            [
                html.H1("Bienvenue sur le Dashboard"),
                html.P("Ceci est la page d'accueil."),
            ]
        )
    elif pathname == "/stats":
        return html.Div(
            [
                html.H1("Statistiques"),
                html.P("Ici, vous pouvez voir les statistiques."),
            ]
        )
    elif pathname == "/about":
        return html.Div(
            [
                html.H1("À propos"),
                html.P("Ceci est une application Dash avec une Navbar."),
            ]
        )
    else:
        return html.Div(
            [
                html.H1("404"),
                html.P("Page non trouvée."),
            ]
        )
