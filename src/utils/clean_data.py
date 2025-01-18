import os
import pandas as pd
from typing import Dict

def clean_data(input_file: str) -> pd.DataFrame:
    """
    Nettoie les données du fichier d'entrée.

    Args:
        input_file (str): Chemin du fichier CSV à nettoyer

    Raises:
        KeyError: Si des colonnes obligatoires sont manquantes
        Exception: Pour toute autre erreur de traitement

    Returns:
        None: Sauvegarde le fichier nettoyé dans data/cleaned/
    """
    print("Le nettoyage commence...")

    try:
        # Chargement des données
        data = pd.read_csv(input_file)
        print(f"Colonnes disponibles dans le fichier : {list(data.columns)}")

        # Nettoyer les colonnes pour enlever les guillemets et caractères spéciaux
        data.columns = data.columns.str.strip().str.replace(
            r"[^\w\s]", "", regex=True
        )  # Supprimer les caractères spéciaux
        print(f"Colonnes après nettoyage : {list(data.columns)}")

        # Création du répertoire de sortie
        output_dir = "data/cleaned"
        os.makedirs(output_dir, exist_ok=True)  # Crée le dossier si nécessaire

        # Renommer la colonne spécifiée (si nécessaire)
        column_mapping: Dict[str, str] = {
            # Exemple de renaming si nécessaire
            # 'ancien_nom': 'nouveau_nom'
        }
        data.rename(columns=column_mapping, inplace=True)
        print(f"Colonnes après renommage : {list(data.columns)}")

        # Colonnes obligatoires
        colonnes_obligatoires = [
            "Latitude",
            "Longitude",
            "Total Damage Adjusted 000 US",
            "Total Affected",
            "Start Day",
            "End Month",
            "End Day",
        ]

        # Vérification des colonnes obligatoires
        colonnes_absentes = [
            col for col in colonnes_obligatoires if col not in data.columns
        ]
        if colonnes_absentes:
            raise KeyError(
                f"Les colonnes suivantes sont absentes : {colonnes_absentes}"
            )

        # Suppression des lignes avec des valeurs manquantes
        data = data.dropna(subset=colonnes_obligatoires)

        print("Suppression des colonnes inutiles...")
        colonnes_a_supprimer = [
            "External IDs",
            "Event Name",
            "Historic",
            "Origin",
            "Associated Types",
            "Last Update",
            "Entry Date",
            "Admin Units",
            "CPI",
            "Total Deaths",
            "No. Injured",
            "No. Affected",
            "No. Homeless",
            "Reconstruction Costs (000 US$)",
            "Reconstruction Costs, Adjusted (000 US$)",
            "Insured Damage (000 US$)",
            "Insured Damage, Adjusted (000 US$)",
            "Total Damage (000 US$)",
        ]
        colonnes_existes = [col for col in colonnes_a_supprimer if col in data.columns]
        if colonnes_existes:
            data = data.drop(columns=colonnes_existes)
            print(f"Colonnes supprimées : {', '.join(colonnes_existes)}")

        # Sauvegarde des données nettoyées
        output_csv = os.path.join(output_dir, "cleaned_data.csv")
        data.to_csv(output_csv, index=False, encoding="utf-8")
        print(f"Le fichier nettoyé est sauvegardé sous '{output_csv}'.")

    except KeyError as e:
        print(f"Erreur de colonnes : {e}")
        raise
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        raise
