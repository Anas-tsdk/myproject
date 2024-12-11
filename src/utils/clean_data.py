import os
import pandas as pd

def clean_data(input_file):
    print("Le nettoyage commence...")

    try:
        # Chargement des données
        data = pd.read_csv(input_file)
        print(f"Colonnes disponibles dans le fichier : {list(data.columns)}")

        # Création du répertoire de sortie
        output_dir = "data/cleaned"
        os.makedirs(output_dir, exist_ok=True)  # Crée le dossier si nécessaire

        # Nettoyer les noms des colonnes pour éviter les problèmes liés aux guillemets
        data.columns = data.columns.str.replace(r'^[\'"]|[\'"]$', '', regex=True)

        # Colonnes obligatoires
        colonnes_obligatoires = [
            'Latitude', 'Longitude', "Total Damage, Adjusted ('000 US$)",
            'Total Affected', 'Start Day', 'End Month', 'End Day'
        ]

        # Vérification des colonnes obligatoires
        colonnes_absentes = [col for col in colonnes_obligatoires if col not in data.columns]
        if colonnes_absentes:
            raise KeyError(f"Les colonnes suivantes sont absentes : {colonnes_absentes}")

        # Suppression des lignes avec des valeurs manquantes
        data = data.dropna(subset=colonnes_obligatoires)

        print("Suppression des colonnes inutiles...")
        colonnes_a_supprimer = [
            'External IDs', 'Event Name', 'Historic', 'Origin', 'Associated Types',
            'Last Update', 'Entry Date', 'Admin Units', 'CPI', 'Total Deaths',
            'No. Injured', 'No. Affected', 'No. Homeless', 'Reconstruction Costs (\'000 US$)',
            'Reconstruction Costs, Adjusted (\'000 US$)', 'Insured Damage (\'000 US$)',
            'Insured Damage, Adjusted (\'000 US$)', 'Total Damage (\'000 US$)'
        ]
        colonnes_existes = [col for col in colonnes_a_supprimer if col in data.columns]
        if colonnes_existes:
            data = data.drop(columns=colonnes_existes)
            print(f"Colonnes supprimées : {', '.join(colonnes_existes)}")

        # Sauvegarde des données nettoyées
        output_csv = os.path.join(output_dir, "cleaned_data.csv")
        data.to_csv(output_csv, index=False, encoding='utf-8')
        print(f"Le fichier nettoyé est sauvegardé sous '{output_csv}'.")

    except KeyError as e:
        print(f"Erreur de colonnes : {e}")
        raise
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        raise
