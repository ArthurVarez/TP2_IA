# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:43:02 2021

@author: robin
"""

from Grille import Grille
from Solveur import Solveur
import time

grille = Grille()

solveur = Solveur(grille, True)
print("Avant\n")
grille.afficherGrille()
t1 = time.time()
solveur.resoudreSudodu()
t2 = time.time()
print("temps : {}".format(t2-t1))
print("\nApres\n")
grille.afficherGrille()

