import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Convertisseur code Markdown en HTML")
parser.add_argument("-i", "--input-directory", help="Chemin du dossier contenant les fichiers sources Markdowns")
parser.add_argument("-o", "--output-directory", help="Chemin du dossier qui contiendra les fichiers générés")   
parser.add_argument("-t", "--template-directory", action="store_true", help="Chemin du dossier template")
parser.parse_args()
args=parser.parse_args()

dossier_source=args.input_directory
dossier_destination=args.output_directory

p=Path(dossier_source)
liste_fichiers=p.glob('**/*.markdown')

for fichier in liste_fichiers:
    texte_remplacement=""
    with open(fichier, 'r', encoding='utf-8') as mon_fichier:
        for ligne in mon_fichier:
            new_ligne=""
            # Gestion des titres
            if '#' in ligne:
                nb_diese=ligne.count('#')
                balise="<h{}>".format(nb_diese)
                new_ligne=balise+ligne[nb_diese:-1]+(balise[:1]+'/'+balise[1:])+'\n'
            print(new_ligne)
            