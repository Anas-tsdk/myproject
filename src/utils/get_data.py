import requests
import pandas as pd
from io import BytesIO
import os


def get_data()-> str:
    """
    Télécharge et convertit les données Excel en CSV.

    Returns:
        str: Chemin du fichier CSV créé

    Raises:
        Exception: Si le téléchargement échoue
    """
    # URL du fichier .xlsx sur GitHub
    url = "https://github.com/InesR91/data_storm_EM_DAT/raw/main/public_emdat_2024-12-03.xlsx"

    # Télécharger le fichier
    print("Téléchargement du fichier Excel...")
    response = requests.get(url)

    if response.status_code == 200:
        # Lecture du fichier Excel en mémoire
        print("Fichier téléchargé avec succès ! Conversion en CSV...")
        excel_data = BytesIO(response.content)

        # Lire le fichier Excel avec pandas
        df = pd.read_excel(
            excel_data, sheet_name=None
        )  # sheet_name=None pour lire toutes les feuilles

        # Créer le dossier 'data/raw' si nécessaire
        output_dir = "data/raw"
        os.makedirs(
            output_dir, exist_ok=True
        )  # Crée le dossier si ce n'est pas déjà fait

        # Sauvegarder le fichier CSV dans le dossier 'data/raw'
        output_csv = os.path.join(output_dir, "rawdata.csv")

        # Sauvegarder le contenu dans un fichier CSV
        with open(output_csv, "w", newline="", encoding="utf-8") as csv_file:
            df_all_sheets = pd.concat(
                df.values(), ignore_index=True
            )  # Si plusieurs feuilles, les concaténer
            df_all_sheets.to_csv(csv_file, index=False)

        print(f"Le fichier a été converti et sauvegardé sous le nom {output_csv}.")
        return output_csv  # Retourne le chemin du fichier CSV
    else:
        raise Exception(
            f"Erreur lors du téléchargement du fichier : {response.status_code}"
        )
