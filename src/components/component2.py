import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc

data_file = "data/cleaned/cleaned_data.csv"
data_global = pd.read_csv(data_file)
data_global["Start Year"] = pd.to_numeric(data_global["Start Year"], errors="coerce")

# Définir les échelles fixes
TOUS_LES_PAYS = sorted(data_global["Country"].unique())
MAX_TEMPETES_GLOBAL = data_global["Country"].value_counts().max()


def afficher_histogramme(start_year, end_year):
    """
    Crée un histogramme des tempêtes par pays.

    Args:
        start_year (int): Année de début
        end_year (int): Année de fin

    Returns:
        html.Div: Composant avec l'histogramme
    """
    # Filtrer les données pour la période sélectionnée
    data_filtered = data_global[
        (data_global["Start Year"] >= start_year)
        & (data_global["Start Year"] <= end_year)
    ]

    # Compter les tempêtes pour la période sélectionnée
    tempetes_periode = pd.Series(
        0, index=TOUS_LES_PAYS
    )  # Initialiser à 0 pour tous les pays
    counts = data_filtered["Country"].value_counts()
    tempetes_periode.update(counts)  # Mettre à jour avec les valeurs réelles

    fig = go.Figure(
        data=[go.Bar(x=TOUS_LES_PAYS, y=tempetes_periode.values, marker_color="blue")]
    )

    fig.update_layout(
        title=f"Nombre de Tempêtes par Pays de {start_year} à {end_year}",
        xaxis_title="Pays",
        yaxis_title="Nombre de Tempêtes",
        xaxis_tickangle=45,
        yaxis=dict(range=[0, MAX_TEMPETES_GLOBAL], fixedrange=True),
        xaxis=dict(fixedrange=True, categoryorder="array", categoryarray=TOUS_LES_PAYS),
        height=1000,
        width=900,
        autosize=False,
    )

    return html.Div([dcc.Graph(figure=fig, config={"displayModeBar": False})])
