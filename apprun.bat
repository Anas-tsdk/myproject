@echo off
REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Installer les d�pendances depuis requirements.txt
pip install -r requirements.txt

REM Lancer le script Python main.py
python main.py

