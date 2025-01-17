import pandas as pd
import plotly.express as px
from dash import html, dcc

def affiche_nuages():

    data_path = "data/cleaned/cleaned_data.csv"
    data = pd.read_csv(data_path)
    
    # Vérifier que la colonne 'OFDA/BHA Response' existe
    if 'OFDABHA Response' not in data.columns:
        print("La colonne 'OFDA/BHA Response' n'existe pas dans le fichier.")
        return
    
    # Vérifier que les colonnes nécessaires sont présentes
    if 'Total Affected' not in data.columns or 'Total Damage Adjusted 000 US' not in data.columns:
        print("Les colonnes 'Total Affected' ou 'Total Damage Adjusted 000 US' sont manquantes.")
        return
    
    # Supprimer les lignes avec des valeurs manquantes dans les colonnes importantes
    data = data.dropna(subset=['Total Affected', 'Total Damage Adjusted 000 US'])
    
    # Création du scatter plot
    fig = px.scatter(data, x="Total Affected", 
                     y="Total Damage Adjusted 000 US", 
                     title="Impact humain vs Aide reçue",
                     labels={"Total Affected": "Total Affected", "Total Damage Adjusted 000 US": "Total Damage Adjusted 000 US"}, 
                     color='OFDABHA Response', 
                     symbol='Disaster Type')

    # Retourner le graphique
    return html.Div([
        dcc.Graph(
            figure=fig,
            style={'height': '600px'}
        )
    ])
