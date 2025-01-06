import folium
from dash import html
import pandas as pd
import requests
import os

# Fonction pour afficher la carte
def afficher_map(colonne):
    # Charger les données
    data_file = "data/cleaned/cleaned_data.csv"
    data = pd.read_csv(data_file)

    # Vérifier si le fichier GeoJSON existe déjà, sinon le télécharger
    geojson_file = "src/world_countries.json"
    if not os.path.exists(geojson_file):
        print("Téléchargement du fichier GeoJSON...")
        url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/world-countries.json"
        response = requests.get(url)
        with open(geojson_file, "wb") as f:
            f.write(response.content)
        print("Téléchargement terminé.")

    data.columns = data.columns.str.replace('"', '', regex=True)  # Supprimer les guillemets
    # Vérifier que la colonne existe dans les données
    if colonne not in data.columns:
        raise ValueError(f"La colonne '{colonne}' n'existe pas dans les données.")

     # Convertir la colonne en numérique, remplacer les erreurs par NaN, puis remplacer les NaN par 0
    data[colonne] = pd.to_numeric(data[colonne], errors='coerce')
    data[colonne] = data[colonne].fillna(0)  # Remplacer NaN par 0 (sans inplace)

    # Ajuster les bins (seuils) en fonction des données : ajustez selon vos besoins
    min_value = data[colonne].min()
    max_value = data[colonne].max()

    # Adapter les seuils (bins) en fonction de la plage des valeurs
    threshold_scale = [min_value, max_value / 4, max_value / 2, 3 * max_value / 4, max_value]

   # Créer une carte centrée
    coords = (0, 0)
    map = folium.Map(
        location=coords,
        tiles='OpenStreetMap',
        zoom_start=2,
        min_zoom=2,  # Définir un zoom minimal
        max_bounds=True
    )


  



    # Ajouter une carte choroplèthe avec une échelle définie
    folium.Choropleth(
        geo_data="src/world_countries.json",  # Chemin du fichier GeoJSON
        name="choropleth",
        data=data,
        columns=["Country", colonne],  # Utiliser la colonne de la donnée passée
        key_on="feature.properties.name",
        fill_color="Reds",  # Palette de couleurs rouges
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=f"Nombre total {colonne}",
        threshold_scale=threshold_scale,  # Utilisation des seuils définis
        legend_position="bottomright",  # Positionner la légende en bas à droite
        control_scale=True  # Ajouter un contrôle de l'échelle
    ).add_to(map)

  
    # Sauvegarder la carte dans un fichier HTML
    map.save(outfile="src/map.html")

    # Retourner un composant Dash contenant la carte
    return html.Iframe(
        srcDoc=open("src/map.html", "r").read(),
        width="60%",
        height="600px",
        style={"border": "none"}
    )
