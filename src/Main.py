# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:43:02 2021

@author: robin
"""

from Grille import Grille
from Solveur import Solveur
import time
import glob
import os
def afficherListeSudoku():
    for fichier in glob.glob("../sudokus/*.txt"):
        print(fichier)
def verifierFichier(fichier):
    return os.path.isfile("../sudokus/"+fichier+".txt")

continuer = True
fichierInvalide= True
grille = Grille()
solveur = Solveur()
print("Bienvenue dans le solveur de sudoku !")
while(continuer):
    print("Choisissez le sudoku à résoudre (ex: tapez sudoku1 pour sudoku1.txt)\n")
    afficherListeSudoku()
    fichier = input()
    fichierInvalide=True
    while(fichierInvalide):
        if(verifierFichier(fichier)):
            fichierInvalide=False
            grille.setGrille(fichier)
            print("Vous avez choisi le sudoku suivant à résoudre:\n")
            grille.afficherGrille()
            print("Lancement de la résolution ...")
            solveur.setGrille(grille)
            grille.grille=solveur.backtrackingSearchMRV_LCV()
            print("Affichage de la solution")
            grille.afficherGrille()
            continuer=input("Souhaitez-vous continuer à résoudre des sudokus ? 1 - Oui 2 - Non\n")=="1"

        else:
            print("Fichier inexistant ! Veuillez réessayer !")
            fichierInvalide=True


