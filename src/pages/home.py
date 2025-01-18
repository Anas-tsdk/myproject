from dash import html, dcc


def home_page()-> html.Div:
    """
    Crée la page d'accueil avec description.

    Returns:
        html.Div: Composant contenant la présentation et les éléments interactifs
    """
    # Styles communs
    common_font = "'Helvetica Neue', Arial, sans-serif"

    container_style = {
        "maxWidth": "800px",
        "margin": "0 auto",
        "padding": "40px 20px",
        "fontFamily": common_font,
    }

    title_style = {
        "color": "#2C3E50",
        "fontSize": "32px",
        "textAlign": "center",
        "marginBottom": "30px",
        "fontWeight": "500",
        "letterSpacing": "0.5px",
    }

    description_style = {
        "color": "#34495E",
        "fontSize": "16px",
        "lineHeight": "1.6",
        "marginBottom": "40px",
        "fontWeight": "300",
    }

    section_style = {
        "backgroundColor": "white",
        "padding": "25px",
        "borderRadius": "8px",
        "boxShadow": "0 2px 4px rgba(0,0,0,0.1)",
        "marginBottom": "30px",
    }

    label_style = {
        "color": "#2C3E50",
        "fontSize": "18px",
        "fontWeight": "500",
        "marginBottom": "15px",
        "display": "block",
    }

    return html.Div(
        children=[
            html.H1("Les Catastrophes Naturelles", style=title_style),
            html.P(
                [
                    "Ce tableau de bord interactif permet d'explorer l'impact des catastrophes naturelles à l'échelle mondiale. À travers une carte choroplèthe, vous pouvez visualiser les régions les plus affectées en fonction de plusieurs critères, tels que le nombre de personnes touchées, les dommages économiques ou la fréquence des tempêtes. ",
                    "De plus, un histogramme présente la répartition des catastrophes naturelles sur une période donnée. Vous pouvez personnaliser la période d'analyse en ajustant les curseurs. Ce tableau de bord contient également un graphique qui présente la répartition des différents types de catastrophes et un scatter plot pour évaluer l'impact des tempêtes sur les populations, ainsi que les aides qu'elles ont reçues.",
                ],
                style=description_style,
            ),
            html.Div(
                [
                    html.Label(
                        "Sélectionnez la période d'analyse :", style=label_style
                    ),
                    dcc.RangeSlider(
                        id="date-slider",
                        min=2000,
                        max=2023,
                        step=1,
                        marks={
                            i: {"label": str(i), "style": {"color": "#2C3E50"}}
                            for i in range(2000, 2024, 2)
                        },
                        value=[2000, 2023],
                        className="slider",
                    ),
                ],
                style=section_style,
            ),
            html.Div(
                [
                    html.H2(
                        "Distribution des Catastrophes",
                        style={**label_style, "marginBottom": "20px"},
                    ),
                    html.P(
                        "Ce graphique montre la répartition des catastrophes naturelles sur la période sélectionnée.",
                        style={
                            "color": "#666",
                            "marginBottom": "20px",
                            "fontSize": "14px",
                        },
                    ),
                    html.Div(id="histogram-container", style={"marginTop": "20px"}),
                ],
                style=section_style,
            ),
        ],
        style=container_style,
    )
