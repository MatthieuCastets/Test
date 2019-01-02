import argparse
import re
import os
from pathlib import Path

parser = argparse.ArgumentParser(description="Convertisseur code Markdown en HTML")
parser.add_argument("-i", "--input-directory", help="Chemin du dossier contenant les fichiers sources Markdowns")
parser.add_argument("-o", "--output-directory", help="Chemin du dossier qui contiendra les fichiers générés")
parser.add_argument("-t", "--template-directory", action="store_true", help="Chemin du dossier template")
parser.parse_args()
args=parser.parse_args()

if args.input_directory is None or not os.path.isdir(args.input_directory):
    print("Veuillez renseigner un repertoire des fichiers source markdown valide")
    exit()

dossier_source=args.input_directory
dossier_destination=args.output_directory
print("Dossier source :", dossier_source)
chemin_dossier_source=Path(dossier_source)
chemin_dossier_destination=Path(dossier_destination)

liste_fichiers=chemin_dossier_source.glob('**/*.markdown')

is_liste=False
expression_url=r"(http(s)?://[a-z0-9]+\.[a-z0-9]+)"

for fichier in liste_fichiers:
    texte_remplacement=""
    with open(fichier, 'r', encoding='utf-8') as mon_fichier:
        for ligne in mon_fichier:
            new_ligne=ligne
            # Gestion des titres
            if '#' in new_ligne:
                nb_diese=new_ligne.count('#')
                balise="<h{}>".format(nb_diese)
                new_ligne=balise+new_ligne[nb_diese:-1]+(balise[:1]+'/'+balise[1:])+'\n'
            # Gestion des listes
            if new_ligne[0]=='*':
                if not is_liste:
                    texte_remplacement += "<ul>\n"
                    is_liste=True
                new_ligne="<li>"+ligne[1:].strip()+"</li>\n"         
            elif is_liste:
                texte_remplacement+="</ul>\n"
                is_liste=False
            # Gestion des textes importants
            while '*' in new_ligne:
                index_etoile=new_ligne.index('*')
                new_ligne=new_ligne[:index_etoile]+"<em>"+ new_ligne[index_etoile+1:]
                index_etoile=new_ligne.index('*')
                new_ligne=new_ligne[:index_etoile]+"</em>"+ new_ligne[index_etoile+1:]
            # Gestion des URLs
            if re.search(expression_url, new_ligne) is not None:
                new_ligne=re.sub(expression_url, "<a href=\"\\1\">\\1</a>", new_ligne)
            
            texte_remplacement+=new_ligne

        print(texte_remplacement)
