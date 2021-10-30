# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:43:02 2021

@author: robin
"""

from Grille import Grille
from Solveur import Solveur

grille = Grille("sudoku2")

solveur = Solveur(grille, False)
print("Avant\n")
grille.afficherGrille()
solveur.resoudreSudodu()
print("\nApres\n")
grille.afficherGrille()

