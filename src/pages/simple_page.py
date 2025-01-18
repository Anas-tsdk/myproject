from dash import html, dcc
from src.components.component4 import affiche_nuages
from src.components.component3 import afficher_camembert


def simple_page():
    """
    Crée la page des visualisations avec composants interactifs.

    Returns:
        html.Div: Composant contenant les trois visualisations
    """

    # Styles communs
    common_font = "'Helvetica Neue', Arial, sans-serif"
    title_style = {
        "color": "#2C3E50",
        "fontSize": "32px",
        "fontFamily": common_font,
        "fontWeight": "500",
        "textAlign": "center",
        "marginBottom": "30px",
        "letterSpacing": "0.5px",
    }
    section_style = {
        "marginBottom": "50px",
        "padding": "20px",
        "backgroundColor": "white",
        "borderRadius": "8px",
        "boxShadow": "0 2px 4px rgba(0,0,0,0.1)",
    }
    radio_style = {
        "backgroundColor": "white",
        "padding": "15px",
        "borderRadius": "8px",
        "boxShadow": "0 2px 4px rgba(0,0,0,0.1)",
        "position": "absolute",
        "top": "400px",
        "right": "90px",
        "fontFamily": common_font,
        "color": "#2C3E50",
    }

    return html.Div(
        [
            # Section Carte
            html.Div(
                [
                    html.H1("Carte du Monde", style=title_style),
                    html.Div(id="carte-container"),
                    dcc.RadioItems(
                        id="data-toggle",
                        options=[
                            {"label": "Total Affecté", "value": "Total Affected"},
                            {
                                "label": "Dégâts Totaux en $",
                                "value": "Total Damage Adjusted 000 US",
                            },
                            {
                                "label": "Nombre de Tempêtes",
                                "value": "Classification Key",
                            },
                        ],
                        value="Total Affected",
                        labelStyle={
                            "display": "block",
                            "marginBottom": "10px",
                            "cursor": "pointer",
                            "fontFamily": common_font,
                        },  # Afficher les labels
                        style=radio_style,
                    ),
                ],
                style=section_style,
            ),
            # Section Camembert
            html.Div(
                [
                    html.H1("Répartition des Types de Catastrophes", style=title_style),
                    afficher_camembert(),  # Afficher le graphique camembert
                ],
                style=section_style,
            ),
            # Section pour le graphique nuage de points (scatterplot)
            html.Div(
                [
                    html.H1("Impact humain vs Aide reçue", style=title_style),
                    affiche_nuages(),  # Afficher le graphique nuage de point
                ],
                style=section_style,
            ),
        ],
        style={
            "maxWidth": "1200px",
            "margin": "0 auto",
            "padding": "20px",
            "backgroundColor": "#F8F9FA",
            "minHeight": "100vh",
            "fontFamily": common_font,
        },
    )
