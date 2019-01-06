# Conversion de fichier markdown en fichier HTML

Ce programme permet de générer à partir d'un dossier de fichiers markdown, des fichiers html qui appairetront dans le dossier voulu.

Ce programme ne convertit pas toutes les expressions existantes, il s'occupe juste des convertir les expressions principales, c'est à dire :
* Les titres
* Les listes non ordonnées
* Les URLs
* Les textes importants

Lors de l'appel à ce programme, il y a différents paramètres à prendre en compte :
* *--input-directory* ou *-i* : Dossier contenant les fichiers sources markdowns
* *--output-directory* ou *-o* : Dossier dans lequel seront générés les fichiers HTML
* *--template-directory* ou *-t* (facultatif) : le dossier contenant le modèle des pages wab à compléter
Pour les chemins des dossiers, on peut soit utiliser le chemin absolu soit le chemin relatif.

Les noms des fichiers générés reprennent le nom du fichier source associé. Juste l'extension change de markdown à HTML. 

## Contraintes

Les expressions ne peuvent être traduit en HTML que si elles respectent le schéma suivant :
* *Titre* : Seul les lignes commençant par des # sont considérés comme des titres et le nombre de # représente le niveu du titre
* *Listes non ordonnées* : Le programme considère comme liste non ordonnée toute ligne commençant par *.
* *Textes importants* : Les textes importants seront considérés comme tel pour tout ensemble de caractère entourés par deux *. 

Il est aussi important de préciser que si l'on met un mot important en début de ligne, cela sera considéré comme une liste d'un seul élément à la place d'un mot important à cause d'une erreur de conception.

Il est obligatoire de mentionner un dossier source et un dossier de réception lorsque l'on fait appel au programme.

Seul les fichiers d'extension *markdown* sont reconnus par le programme afin d'être convertit en HTML. 
 
