import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc

def afficher_histogramme(start_year, end_year):
 
    data_file = "data/cleaned/cleaned_data.csv"
    data = pd.read_csv(data_file)

   
    data['Start Year'] = pd.to_numeric(data['Start Year'], errors='coerce')
    
    data_filtered = data[(data['Start Year'] >= start_year) & (data['Start Year'] <= end_year)]  # Filtrer les données en fonction de l'intervalle d'années sélectionné
    
    tempetes_par_annee = data_filtered['Start Year'].value_counts().sort_index()# calculer le nombre de catastrophes par année filtrée

       
    fig = go.Figure(data=[go.Bar(
            x=tempetes_par_annee.index,  # années
            y=tempetes_par_annee.values,  # nombre de catastrophes par année
            marker=dict(color='blue')  
        )])

       
    fig.update_layout(
            title=f"Nombre de Tempêtes de {start_year} à {end_year}",
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

   