# -*- coding: utf-8 -*-

from dash import html


def header():
    """
    Crée l'en-tête du dashboard.

    Returns:
        html.Header: Composant header avec titre et sous-titre
    """
    header_style = {
        "backgroundColor": "#F8F9FA",
        "padding": "40px 20px",
        "marginBottom": "30px",
        "borderBottom": "3px solid #3498DB",
        "textAlign": "center",
        "fontFamily": "'Helvetica Neue', Arial, sans-serif",
    }
    title_style = {
        "color": "#2C3E50",
        "fontSize": "32px",
        "marginBottom": "15px",
        "fontWeight": "500",
        "letterSpacing": "0.5px",
    }
    subtitle_style = {
        "color": "#34495E",
        "fontSize": "16px",
        "margin": "0",
        "fontWeight": "300",
        "maxWidth": "800px",
        "marginLeft": "auto",
        "marginRight": "auto",
    }
    return html.Header(
        children=[
            html.H1(
                "Dashboard Tempêtes et Impacts sur la Santé Publique", style=title_style
            ),
            html.P(
                "Visualisation des données sur les tempêtes et leurs effets sur la santé publique.",
                style=subtitle_style,
            ),
        ],
        style=header_style,
    )
