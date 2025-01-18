import folium
from dash import html
import pandas as pd
import requests
import os
import json
import numpy as np

def afficher_map(colonne):
    """
    Crée une carte géographique interactive affichant des données spécifiques.

    Args:
        colonne (str): Le nom de la colonne dans les données qui contient les informations à visualiser sur la carte.
    
    Returns:
        html.Iframe: Un composant HTML contenant la carte générée sous forme d'iframe.
    """

    # Charger les données
    data_file = "data/cleaned/cleaned_data.csv"
    data = pd.read_csv(data_file)
    print("Colonnes du fichier CSV :")
    print(data.columns)

    # Vérifier si le fichier GeoJSON existe déjà, sinon le télécharger
    geojson_file = "src/world_countries.json"
    if not os.path.exists(geojson_file):
        print("Téléchargement du fichier GeoJSON...")
        url = "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/world-countries.json"
        response = requests.get(url)
        with open(geojson_file, "wb") as f:
            f.write(response.content)
        print("Téléchargement terminé.")

    # Nettoyer les noms de colonnes pour éviter les erreurs dues aux caractères spéciaux
    

    # Vérifier que la colonne existe dans les données
    if colonne not in data.columns:
        raise ValueError(f"La colonne '{colonne}' n'existe pas dans les données.")
    
    # Afficher les colonnes pour vérifier la présence de 'Country'
    print(data.columns)

    # Convertir la colonne en numérique, remplacer les erreurs par NaN, puis remplacer les NaN par 0
    data[colonne] = pd.to_numeric(data[colonne], errors='coerce')
    data[colonne] = data[colonne].fillna(0)  # Remplacer NaN par 0 

    # Ajuster les bins (seuils) en fonction des données
    min_value = data[colonne].min()
    max_value = data[colonne].max()

    with open(geojson_file, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    geojson_countries = [feature['properties']['name'] for feature in geojson_data['features']]
    csv_countries = data['Country'].unique()

    # Comparer les noms et faire un mapping pour associer les noms des pays
    missing_from_geojson = [country for country in csv_countries if country not in geojson_countries]
    missing_from_csv = [country for country in geojson_countries if country not in csv_countries]

    print("Pays présents dans le CSV mais absents dans le GeoJSON:", missing_from_geojson)
    print("Pays présents dans le GeoJSON mais absents dans le CSV:", missing_from_csv)

    mapping = {
        "Russian Federation": "Russia",
        "Türkiye": "Turkey",
        "Taiwan (Province of China)": "Taiwan",
        "Iran (Islamic Republic of)": "Iran",
        "Bolivia (Plurinational State of)": "Bolivia",
        "Viet Nam": "Vietnam",
        "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
        "Democratic People's Republic of Korea": "North Korea",
        "Republic of Korea": "South Korea",
        "Czechia": "Czech Republic",
        "Serbia": "Republic of Serbia",
        "Venezuela (Bolivarian Republic of)": "Venezuela",
        "North Macedonia": "Macedonia",
        "Timor-Leste": "East Timor",
        "Syrian Arab Republic": "Syria",
    }
    # Appliquer le mapping pour remplacer les noms de pays
    data['Country'] = data['Country'].replace(mapping)

    # Supprimer les pays qui ne peuvent pas être mappés
    data = data[data['Country'].notna()]

    # Adapter les seuils (bins) en fonction de la plage des valeurs
    threshold_scale = [min_value, max_value / 4, max_value / 2, 3 * max_value / 4, max_value]

    # Cas spécifiques pour les colonnes
    if colonne == "Total Affected":
        affected_counts = data.groupby('Country')[colonne].sum().reset_index(name='Total')
        data = data.merge(affected_counts, on='Country', how='left')
        min_value = affected_counts['Total'].min()
        max_value = affected_counts['Total'].max()
        threshold_scale = [min_value, min_value + (max_value - min_value) * 0.05, 
                       min_value + (max_value - min_value) * 0.1, 
                       min_value + (max_value - min_value) * 0.2, 
                       max_value]

    if colonne == "Total Damage Adjusted 000 US":
        damage_counts = data.groupby('Country')[colonne].sum().reset_index(name='Total Damage Adjusted')
        data = data.merge(damage_counts, on='Country', how='left')
        min_value = damage_counts['Total Damage Adjusted'].min()
        max_value = damage_counts['Total Damage Adjusted'].max()
        threshold_scale = [min_value, min_value + (max_value - min_value) * 0.05, 
                       min_value + (max_value - min_value) * 0.1, 
                       min_value + (max_value - min_value) * 0.2, 
                       max_value]

    if colonne == "Classification Key":
        storm_counts = data.groupby('Country').size().reset_index(name='Total Tempêtes')
        data = data.merge(storm_counts, on='Country', how='left')
        min_value = storm_counts['Total Tempêtes'].min()
        max_value = storm_counts['Total Tempêtes'].max()
        threshold_scale = [min_value, max_value / 4, max_value / 2, 3 * max_value / 4, max_value]

    # Créer la carte
    coords = (0, 0)
    map = folium.Map(location=coords, tiles='CartoDB Positron', zoom_start=2, min_zoom=2, max_bounds=True)

    folium.Choropleth(
        geo_data="src/world_countries.json",
        name="choropleth",
        data=data,
        columns=["Country", 
                     "Total Tempêtes" if colonne == "Classification Key" 
                     else "Total" if colonne == "Total Affected" 
                     else "Total Damage Adjusted" if colonne == "Total Damage Adjusted 000 US"
                     else colonne],
        key_on="feature.properties.name",
        fill_color="Reds",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=f"Nombre total {colonne}",
        threshold_scale=threshold_scale,
        legend_position="bottomright",
        control_scale=True
    ).add_to(map)

    map.save(outfile="src/map.html")

    return html.Iframe(
        srcDoc=open("src/map.html", "r").read(),
        width="60%",
        height="600px",
        style={"border": "none", "display": "block", "margin": "0 auto"}
    )
