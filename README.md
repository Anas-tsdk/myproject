# README
## _Tempêtes et Santé Publique_

## User Guide

Pour déployer et utiliser le dashboard il faut lancer cette commande dans le terminal:

```sh
python main.py
```

## Data

Nous avons utilisé des données provenant de l'[EM-DAT](https://www.emdat.be/) qui contient une base de données sur les catastrophes dans le monde entier. Les données ont été diffusées par le Centre de recherche sur l'épidémiologie des catastrophes (CRED). Cependant les données ne pouvaient pas être téléchargé à partir de notre programme car il fallait se connecter à un compte. Nous avons donc télécharger les données puis mis dans un git pour pouvoir les télécharger à partir de cet endroit lorque l'on lance le programme (sous l'accord de Monsieur PERRET).


## Developer Guide
faire graphique architecture
```mermaid
flowchart TD
    %% Structure principale
    A[Main Application] -->|Dash| B[App Layout]
    B --> C[dcc.Location]
    B --> D[Navbar]
    B --> E[Header]
    B --> F[Page Content Div]
    B --> G[Footer]

    %% Callbacks
    subgraph Callbacks
        H1[update_page_and_map]
        H2[update_map]
        H3[update_histogram]
        H4[update_nuages]
    end
    F -->|Callback| Callbacks
     subgraph Components
        J1[afficher_map]
        J2[afficher_histogramme]
        J3[afficher_camembert]
        J4[affiche_nuages]
    end
    %% Pages et composants
    subgraph Pages
        I1[Home Page]
        I2[About Page]
        I3[Simple Page]
        I2 -->|Uses| J2[afficher_histogramme]
        I3 -->|Uses| J1[afficher_map]
        I3 -->|Uses| J3[afficher_camembert]
        I3 -->|Uses| J4[affiche_nuages]
    end
    H1 -->|"/home"| I1
    H1 -->|"/about"| I2
    H1 -->|"/stats"| I3
    H2 --> J1
    H3 --> J2
    H4 --> J4
```
## Rapport d'analyse
met en avant les principales conclusions extraites des données


## Copyright

Nous déclarons sur l'honneur que le code fourni a été produit par nous même, à l'exception des lignes ci-dessous : 
