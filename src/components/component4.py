import pandas as pd
import plotly.express as px
from dash import html, dcc

def affiche_nuages():

    data_path = "data/cleaned/cleaned_data.csv"
    data = pd.read_csv(data_path)
    
    # Vérifier que la colonne existe
    if 'OFDA/BHA Response' not in data.columns:
        print("La colonne 'OFDA/BHA Response' n'existe pas dans le fichier.")
        return
    

    fig = px.scatter(data, x="Total Affected", 
                     y="Total Damage, Adjusted ('000 US$)", 
                     title="Impact humain vs Aide reçue",
                     labels={"Total Affected": "Total Affected", "Total Damage, Adjusted ('000 US$)": "Total Damage, Adjusted ('000 US$)"}, 
                     color = 'OFDA/BHA Response', 
                     symbol = 'Disaster Type')
    

    return html.Div([
        dcc.Graph(
            figure=fig,
            style={'height': '600px'}
        )
    ])