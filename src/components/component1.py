#graphe map
import folium
from dash import html

def afficher_map():
    # Générer une carte avec Folium
    coords = (0, 0)  # Centre de la carte : coordonnées 0, 0 (équateur et méridien de Greenwich)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=2)

    # Sauvegarder la carte dans un fichier temporaire
    map.save(outfile="src/map.html")  # Assurez-vous que le dossier `assets` existe

    # Retourner un composant Dash contenant la carte
    return html.Iframe(
        srcDoc=open("src/map.html", "r").read(),  # Charger le contenu HTML de la carte
        width="100%",  # Largeur de l'Iframe
        height="600px",  # Hauteur de l'Iframe
        style={"border": "none"}
    )
