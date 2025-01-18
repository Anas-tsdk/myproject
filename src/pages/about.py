from dash import html


def about_page():
    """
    Crée la page 'À propos' avec sections structurées et styles définis.

    Returns:
        html.Div: Composant contenant les sections d'information stylisées
    """
    # Style commun pour tout le site
    common_font = "'Helvetica Neue', Arial, sans-serif"

    # Styles principaux
    title_style = {
        "textAlign": "center",
        "color": "#2C3E50",
        "fontFamily": common_font,
        "fontSize": "32px",
        "fontWeight": "500",
        "marginBottom": "40px",
        "borderBottom": "3px solid #3498DB",
        "paddingBottom": "10px",
        "letterSpacing": "0.5px",
    }

    section_title_style = {
        "fontSize": "24px",
        "fontWeight": "500",
        "color": "#2C3E50",
        "fontFamily": common_font,
        "marginTop": "30px",
        "marginBottom": "20px",
        "paddingLeft": "15px",
        "borderLeft": "4px solid #3498DB",
    }

    text_container_style = {
        "backgroundColor": "white",
        "padding": "20px",
        "borderRadius": "8px",
        "marginBottom": "20px",
        "boxShadow": "0 2px 4px rgba(0,0,0,0.1)",
        "fontFamily": common_font,
        "fontSize": "16px",
        "lineHeight": "1.8",
        "color": "#34495E",
    }

    link_style = {"color": "#3498DB", "textDecoration": "none", "fontWeight": "500"}

    return html.Div(
        [
            # Titre principal
            html.H1("À propos", style=title_style),
            # Section Équipe
            html.H2("Notre équipe", style=section_title_style),
            html.Div(
                [
                    "Ce projet a été réalisé par:",
                    html.Ul(
                        [html.Li("Tsundyk Anastasia"), html.Li("Robin Inès")],
                        style={"listStyleType": "none", "padding": "0"},
                    ),
                ],
                style=text_container_style,
            ),
            # Section Projet
            html.H2("Le projet", style=section_title_style),
            html.Div(
                [
                    "Notre projet permet de visualiser l'impact des catastrophes naturelles sur la santé publique mondiale.",
                    html.Br(),
                    html.Br(),
                    "Nous avons choisi ce sujet d'actualité qui nous concerne tous, particulièrement avec le changement climatique.",
                ],
                style=text_container_style,
            ),
            # Section Données
            html.H2("Nos données", style=section_title_style),
            html.Div(
                [
                    "Les données utilisées proviennent de ",
                    html.A(
                        "emdata",
                        href="https://www.emdat.be/",
                        target="_blank",
                        style=link_style,
                    ),
                ],
                style=text_container_style,
            ),
            # Section Méthodologie
            html.H2("Méthodologie", style=section_title_style),
            html.Div(
                [
                    html.Ul(
                        [
                            html.Li("Collecte et nettoyage des données"),
                            html.Li("Analyse statistique"),
                            html.Li("Création de visualisations interactives"),
                        ],
                        style={"marginLeft": "20px"},
                    )
                ],
                style=text_container_style,
            ),
            # Section Défis
            html.H2("Défis rencontrés", style=section_title_style),
            html.Div(
                [
                    "Au cours du développement, nous avons fait face à plusieurs défis:",
                    html.Ul(
                        [
                            html.Li(
                                "La création et l'optimisation de la carte interactive ont été les étapes les plus complexes. En effet, la carte géographique est liée à un fichier JSON qui sert à générer la carte choroplèthe. Cette carte choroplèthe utilise les données du fichier CSV pour afficher les couleurs correspondant à chaque pays. J'avais initialement associé les noms des pays du fichier CSV avec ceux du fichier JSON. Cependant, cela a causé un problème, car certains pays apparaissaient en noir, sans couleur assignée, et nous ne comprenions pas pourquoi. Après quelques recherches, nous avons découvert que certains pays, après le nettoyage des données, n'avaient plus de valeurs, et que les noms dans le fichier JSON ne correspondaient pas exactement à ceux du CSV. Pour résoudre ce problème, j'ai développé un script permettant de remplacer les noms dans le fichier JSON par ceux présents dans le fichier CSV."
                            ),
                            html.Li(
                                "Le deuxième problème rencontré sur la carte géographique concernait l'échelle. Par exemple, pour les dégâts, la plupart des données se situaient entre la valeur minimale et le premier quart, ce qui ne permettait pas de visualiser suffisamment les variations de couleurs. Pour remédier à cela, j'ai réduit les intervalles de l'échelle, mais cela a eu pour effet de compresser les couleurs dans l'affichage de l'échelle, ce qui a rendu les légendes moins visibles."
                            ),
                            html.Li(
                                [
                                    "Lors de nos recherches, nous avons découvert ",
                                    html.A(
                                        "ce git",
                                        href="https://github.com/em-dat/",
                                        target="_blank",
                                        style=link_style,
                                    ),
                                    " utilisant les mêmes données. Nous avons alors décidé de ne pas nous en inspirer et de proposer une version originale",
                                ]
                            ),
                        ],
                        style={"marginLeft": "20px"},
                    ),
                ],
                style=text_container_style,
            ),
            # Section Remerciements
            html.H2("Remerciements", style=section_title_style),
            html.Div(
                [
                    "Nous tenons à remercier:",
                    html.Ul(
                        [
                            html.Li("Nos professeurs"),
                            html.Li(
                                "Et les visiteurs, pour votre intérêt à notre projet"
                            ),
                        ],
                        style={"marginLeft": "20px"},
                    ),
                ],
                style=text_container_style,
            ),
        ],
        style={
            "maxWidth": "800px",
            "margin": "0 auto",
            "padding": "40px 20px",
            "backgroundColor": "#F8F9FA",
            "borderRadius": "10px",
            "minHeight": "100vh",
        },
    )
