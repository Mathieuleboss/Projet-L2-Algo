#Cette algorithme en Python permet d'extraire le texte d'un fichier PDF spécifié en argument via la ligne de commande et l'affiche dans le terminal.

import fitz
import sys

# Fonction d'extraction du texte depuis un fichier PDF
def extraire_texte_pdf(chemin_fichier):
    texte = ""
    with fitz.open(chemin_fichier) as pdf:
        for page in pdf:
            texte += page.get_text()
    return texte

# Point d'entrée
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erreur : Aucun fichier PDF spécifié. Usage : python extract_text.py <chemin_fichier>")
        sys.exit(1)
    
    chemin_fichier = sys.argv[1]
    
    try:
        texte = extraire_texte_pdf(chemin_fichier)
        print(texte)
    except Exception as e:
        print(f"Erreur lors de l'extraction du texte : {e}")
        sys.exit(1)
