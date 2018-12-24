import argparse

parser = argparse.ArgumentParser(description="Convertisseur code Markdown en HTML")
parser.add_argument("-i", "--input-directory", help="Chemin du dossier contenant les fichiers sources Markdowns")
parser.add_argument("-o", "--output-directory", help="Chemin du dossier qui contiendra les fichiers générés")   
parser.add_argument("-t", "--template-directory", action="store_true", help="Chemin du dossier template")

parser.parse_args()

args=parser.parse_args()

dossier_source=args.input_directory
dossier_destination=args.output_directory
print(dossier_destination)