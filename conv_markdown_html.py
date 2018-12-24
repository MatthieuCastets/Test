import argparse

parser = argparse.ArgumentParser(description="Convertisseur code Markdown en HTML")
parser.add_argument("-i", "--input-directory", help="Dossier contenant les fichiers sources Markdowns")
parser.add_argument("-o", "--output-directory", help="Chemin du dossier qui contiendra les fichiers générés")   
parser.add_argument("-t", "--template-directory", action="store_true", help="Chemin du dossier template")

parser.parse_args()
