# -*- coding: utf-8 -*-

from dash import html

def header():
    return html.Header(
        children=[
            html.H1("Dashboard Tempêtes et Impacts sur la Santé Publique", style={'text-align': 'center', 'color': '#007bff'}),
            html.P("Visualisation des données sur les tempêtes et leurs effets sur la santé publique.", style={'text-align': 'center'})
        ]
    )