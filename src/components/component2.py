import plotly.graph_objects as go
from dash import html, dcc

def afficher_histogramme():
    # Création des données d'exemple
    donnees = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    
 
    fig = go.Figure(data=[go.Histogram(x=donnees)])
    

    fig.update_layout(
        title="Mon Histogramme",
        xaxis_title="Valeurs",
        yaxis_title="Fréquence",
        bargap=0.1 
    )


    return html.Div([
        dcc.Graph(
            figure=fig,
            style={'height': '600px'}
        )
    ])