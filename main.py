import argparse
import markdown2
import os
import re

link_patterns = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]


parser = argparse.ArgumentParser(description='conversion markdown en html')
parser.add_argument("-i","--input-directory", type=str,metavar="",required=True, help= "chemin du fichier source")
parser.add_argument("-o","--output-directory", type=str,metavar="",required= True, help= "chemin du fichier final")
args = parser.parse_args()

fichier_md = args.input_directory #fichiers markdown de depart
fichier_html = args.output_directory #resultat final

contenu_md = os.listdir(fichier_md) #recuperation des fichers markdown dans une liste

def conversion(fichier_md,fichier_html) : #fonction de conversion du markdown vers l'html
    compteur = 0
    for fichier in contenu_md: #lecture des fichiers markdown
        with open(f'{fichier_md}/{fichier}',"r") as file :
            convert_html = markdown2.markdown(file.read()) #conversion markdown en html
            resultat_html= open(f'{fichier_html}/index{compteur}.html',"w") 
            resultat_html.write(convert_html) #conversion markdown en html
            resultat_html.close()
            compteur += 1

conversion(fichier_md,fichier_html) #appel de la fonction 
