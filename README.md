# README
## _Temp�tes et Sant� Publique_

## User Guide

Pour d�ployer et utiliser le dashboard il faut lancer cette commande dans le terminal :

```sh
python main.py
```

## Data

Nous avons utilis� des donn�es provenant de l'[EM-DAT](https://www.emdat.be/) qui contient une base de donn�es sur les catastrophes dans le monde entier. Les donn�es ont �t� diffus�es par le Centre de recherche sur l'�pid�miologie des catastrophes (CRED). Cependant les donn�es ne pouvaient pas �tre t�l�charg� � partir de notre programme car une connexion � un compte �tait n�cessaire. Nous avons donc t�l�charg� les donn�es manuellement, puis les avons int�gr�es dans un d�p�t Git afin de pouvoir les t�l�charger directement lors de l'ex�cution du programme (sous l'accord de Monsieur PERRET).


## Developer Guide
Voici le diagramme de l'architecture de notre application r�alis� avec Mermaid :
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

Notre programme est de type imp�ratif, le code est structur� en fonctions appel�es depuis le programme principal.
## Rapport d'analyse
met en avant les principales conclusions extraites des donn�es


## Copyright

Nous d�clarons sur l'honneur que le code fourni a �t� produit par nous m�me, � l'exception des lignes ci-dessous : 
