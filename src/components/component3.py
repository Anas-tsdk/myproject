import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc


def afficher_camembert():
    """
    Crée un graphique en camembert des types de catastrophes.

    Returns:
        html.Div: Composant Dash contenant le camembert
    """

    data_file = "data/cleaned/cleaned_data.csv"
    data = pd.read_csv(data_file)

    categories = [
        "Geophysical",
        "Hydrological",
        "Meteorological",
    ]  # fitre les trois types de catastrophes
    data_filtered = data[data["Disaster Subgroup"].isin(categories)]

    count_by_type = data_filtered[
        "Disaster Subgroup"
    ].value_counts()  # calcul le nombre de catastrophe pour chaque categorie

    # camembert avec Plotly
    colors = ["#2C3E50", "#3498DB", "#1ABC9C"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=count_by_type.index,  # types de catastrophes
                values=count_by_type.values,  # nombre
                hole=0.3,  # pour avoir un dognut
                marker=dict(colors=colors),  # Appliquer les couleurs
                textinfo="percent",  # Afficher pourcentages
            )
        ]
    )

    fig.update_layout(
        title=None,
        legend_title="Catégories",
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    # Retourner le camembert dans un objet Dash
    return html.Div([dcc.Graph(figure=fig, style={"height": "600px"})])
