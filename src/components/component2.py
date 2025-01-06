import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc

def afficher_histogramme():
 
    data_file = "data/cleaned/cleaned_data.csv"
    data = pd.read_csv(data_file)

   
    data['Start Year'] = pd.to_numeric(data['Start Year'], errors='coerce')

       
    tempetes_par_annee = data['Start Year'].value_counts().sort_index() # calculer le nombre de catastrophes par année

       
    fig = go.Figure(data=[go.Bar(
            x=tempetes_par_annee.index,  # années
            y=tempetes_par_annee.values,  # nombre de catastrophes par année
            marker=dict(color='blue')  
        )])

       
    fig.update_layout(
            title="Nombre de Tempêtes par Année",
            xaxis_title="Année",
            yaxis_title="Nombre de Tempêtes",
            bargap=0.1  # espace entre les barres
        )

        #retourner l'objet Dash pour afficher le graphique
    return html.Div([
            dcc.Graph(
                figure=fig,
                style={'height': '600px'}
            )
        ])

   