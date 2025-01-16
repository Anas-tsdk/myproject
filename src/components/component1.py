import folium
from dash import html
import pandas as pd
import requests
import os
import json

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
    
    # Nettoyer les noms de colonnes pour éviter les espaces ou caractères invisibles
    data.columns = data.columns.str.strip()

    # Afficher les colonnes pour vérifier la présence de 'Country'
    print(data.columns)

    # Convertir la colonne en numérique, remplacer les erreurs par NaN, puis remplacer les NaN par 0
    data[colonne] = pd.to_numeric(data[colonne], errors='coerce')
    data[colonne] = data[colonne].fillna(0)  # Remplacer NaN par 0 

    # Ajuster les bins (seuils) en fonction des données : ajustez selon vos besoins
    min_value = data[colonne].min()
    max_value = data[colonne].max()

    with open(geojson_file, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    geojson_countries = [feature['properties']['name'] for feature in geojson_data['features']]
    csv_countries = data['Country'].unique()

    # Comparer les noms et fait un mapping pour pouvoir associer les noms des pays et afficher les données dans la map 
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
        "United Kingdom of Great Britain and Northern Ireland": "Ireland",
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
    #threshold_scale = [min_value, max_value / 4, max_value / 2, 3 * max_value / 4, max_value]
    threshold_scale = []

    # Si la colonne est "Total Damage", on regroupe les données par pays et on additionne
    if colonne == "Total Damage":
        # Grouper par pays et additionner les valeurs de la colonne 'Total Damage'
        damage_counts = data.groupby('Country')[colonne].sum().reset_index(name='Total D')

        # Mettre à jour 'data' avec les valeurs agrégées
        data = data.merge(damage_counts, on='Country', how='left')

        # Mettre à jour les seuils
        min_value = damage_counts['Total D'].min()
        max_value = damage_counts['Total D'].max()
        threshold_scale = [min_value, 2500000, 5000000, 7500000, max_value]

    # Si la colonne est "Total Affected", on regroupe les données par pays et on additionne
    if colonne == "Total Affected":
        # Grouper par pays et additionner les valeurs de la colonne 'Total Affected'
        affected_counts = data.groupby('Country')[colonne].sum().reset_index(name='Total')

        # Mettre à jour 'data' avec les valeurs agrégées
        data = data.merge(affected_counts, on='Country', how='left')

        # Mettre à jour les seuils
        min_value = affected_counts['Total'].min()
        max_value = affected_counts['Total'].max()
        threshold_scale = [min_value, 500000, 1000000, 1500000, max_value]

        print("Statistiques des 'Total Affected' par pays :")
        print(affected_counts.sort_values('Total', ascending=False))
        print(min_value, max_value)

    if colonne == "Classification Key":
        # Grouper par pays et compter les occurrences
        storm_counts = data.groupby('Country').size().reset_index(name='Total Tempêtes')

        # Mettre à jour data avec les comptages
        data = data.merge(storm_counts, on='Country', how='left')

        # Mettre à jour les seuils
        min_value = storm_counts['Total Tempêtes'].min()
        max_value = storm_counts['Total Tempêtes'].max()
        

        print("Statistiques des tempêtes par pays :")
        print(storm_counts.sort_values('Total Tempêtes', ascending=False))
        print(min_value, max_value)
        threshold_scale = [min_value, max_value/4, max_value/2, 3*max_value/4, max_value]

    

    # Créer la carte
    coords = (0, 0)
    map = folium.Map(
        location=coords,
        tiles='CartoDB Positron',
        zoom_start=2,
        min_zoom=2,  # Définir un zoom minimal
        max_bounds=True
    )

    # Ajouter la carte choroplèthe en fonction de la colonne choisie
    folium.Choropleth(
            geo_data="src/world_countries.json",  # Chemin du fichier GeoJSON
            name="choropleth",
            data=data,
            columns=["Country", 
                     "Total Tempêtes" if colonne == "Classification Key" 
                     else "Total" if colonne == "Total Affected" 
                     else "Total D" if colonne == "Total Damage"
                     else colonne],
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
        style={"border": "none", "display": "block", "margin": "0 auto"}
    )
