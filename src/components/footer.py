# -*- coding: utf-8 -*-

from dash import html


def footer():
    """
    Crée le footer avec copyright et contacts.

    Returns:
        html.Footer: Composant footer avec informations de contact
    """
    return html.Footer(
        children=[
            html.Div(
                children="\u00a9 2024 - Tempêtes et Santé Publique. ines.robin@edu.esiee.fr - anastasia.tsundyk@edu.esiee.fr",
                style={"text-align": "center", "font-size": "12px", "color": "gray"},
            )
        ]
    )
