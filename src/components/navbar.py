from dash import html

"""
Barre de navigation du dashboard.

Définit une navbar avec des liens vers les différentes pages :
Accueil, Graphes, À propos.
"""
navbar = html.Div(
    [
        html.Ul(
            [
                html.Li(
                    html.A("Accueil", href="/home", className="nav-link"),
                    className="nav-item",
                ),
                html.Li(
                    html.A("Graphes", href="/stats", className="nav-link"),
                    className="nav-item",
                ),
                html.Li(
                    html.A("À propos", href="/about", className="nav-link"),
                    className="nav-item",
                ),
            ],
            className="navbar",
            style={
                "listStyleType": "none",  # Enlève les puces de la liste
                "display": "flex",  # Aligne les éléments de manière horizontale
                "justifyContent": "space-around",  # Espace les éléments de manière égale
                "padding": "0",  # Enlève le padding de la liste
                "margin": "0",  # Enlève la marge de la liste
                "fontFamily": "'Helvetica Neue', Arial, sans-serif",  # Police
                "fontSize": "16px",  # Taille
                "fontWeight": "400",  # Epaisseur de police 
            },
        )
    ],
    className="navbar-container",
    style={
        "width": "100%",
        "border": "1px solid #ddd",  # Bordure autour de la navbar
        "boxShadow": "0px 4px 2px -2px gray",  # Ombre légère pour la navbar
        "backgroundColor": "#f8f9fa",
        "padding": "10px 0",  # Padding pour les bords
    },
)
