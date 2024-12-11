import os
import pandas as pd
import requests

def nettoyer_fichier(input_file, output_file):
    print("Le nettoyage commence...")

    try:
        
        data = pd.read_csv(input_file)

        # Suppression des lignes avec des valeurs manquantes dans les colonnes obligatoires
        colonnes_obligatoires = [
            'Latitude', 'Longitude', 'Total Damage Adjusted', 'Total Affected', # modife total damage
            'Start Day', 'End Month', 'End Day'
        ]

        # Supprimer les lignes où certaines colonnes sont vides
        data = data.dropna(subset=colonnes_obligatoires)

        print("Suppression des colonnes inutiles...")
        colonnes_a_supprimer = [
            'External', 'Event Name', 'Historic', 'Origin', 'Associated',
            'Last Update', 'Entry Data', 'Admin Units', 'CPI', 'Total Death',
            'Injure', 'No. Affect', 'No. Homeless', 'Reconstruction', 'Insured',
            'Total Damage', 'AID Contribution','External IDs', 'Reconstruction Costs, Adjusted', 
            'Reconstruction Costs', 'Insured Damage', 'Insured Damage, Adjusted'
            # modife AID Contribution, Reconstruction Costs, Adjusted,Reconstruction Costs , Insured Damage,Insured Damage, Adjusted, Total Damage
        ]
        colonnes_existes = [col for col in colonnes_a_supprimer if col in data.columns]
        if colonnes_existes:
            data = data.drop(columns=colonnes_existes)
            print(f"Colonnes supprimées : {', '.join(colonnes_existes)}")

        print(f"Sauvegarde du fichier nettoyé sous '{output_file}'...")
        data.to_csv(output_file, index=False)
        print(f"Le fichier nettoyé est sauvegardé sous '{output_file}'.")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        raise