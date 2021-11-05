# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 23:45:03 2021

@author: robin
"""
import math, time
class Solveur:
    
    def __init__(self, grille, optimised=True):
        self.grille = grille
        self.optimised = optimised
        
    def resoudreSudodu(self):
        if(self.optimised):
            self.backtrackingSearchMRV_LCV()
        else:
            self.backtrackingSearch()
        
    def backtrackingSearch(self):
        def grilleComplete(grille):
            for x in range(n):
                for y in range(n):
                    if(grille[x][y]==0):
                        return False
            return True

        def selectionnerVariableNonAssignee():
            for x in range(n):
                for y in range(n):
                    if(grille[x][y]==0):
                        return [x,y]

        def getValeursAutorisees(var):
            index = var[0]*n+var[1]
            possibilites = [1,2,3,4,5,6,7,8,9]
            liste_voisins = [[(id-(id%n))//n, id%n] for id, estVoisin in enumerate(csp[index]) if estVoisin]
            valeurs_voisins = [grille[x][y] for x,y in liste_voisins if grille[x][y]!=0]
            return [val for val in possibilites if val not in valeurs_voisins]

        def recursiveBacktracking():
            if(grilleComplete(grille)):
                return grille
            var = selectionnerVariableNonAssignee()
            valeursAutorisees = getValeursAutorisees(var, )
            for value in valeursAutorisees:
                grille[var[0]][var[1]]=value
                result = recursiveBacktracking()
                if(result!=-1):
                    return result
                grille[var[0]][var[1]]=0
            return -1
        
        grille=self.grille.grille
        csp = self.grille.matriceAdjacenceGrapheContrainte
        n=self.grille.n
        return recursiveBacktracking()


    def backtrackingSearchMRV_LCV(self):
        def grilleComplete():
            for x in range(n):
                for y in range(n):
                    if(grille[x][y]==0):
                        return False
            return True


        def selectionnerVariableNonAssignee():
            nBValeurLegales=10
            var=[0,0]
            for x in range(n):
                for y in range(n):          
                    possibilites = getValeursAutorisees([x, y])
                    if(grille[x][y]==0 and len(possibilites)<nBValeurLegales):
                        nBValeurLegales = len(possibilites)
                        var=[x, y]
            return var


        def getValeursAutorisees(var):
            index = var[0]*n+var[1]
            possibilites = [1,2,3,4,5,6,7,8,9]
            liste_voisins = [[(id-(id%n))//n, id%n] for id, estVoisin in enumerate(csp[index]) if estVoisin]
            valeurs_voisins = [grille[x][y] for x,y in liste_voisins if grille[x][y]!=0]
            return [val for val in possibilites if val not in valeurs_voisins]

        def getValeursAutoriseesLCV(var):
            valeurs_autorisees = getValeursAutorisees(var)
            if valeurs_autorisees==[]:
                return []
            compteur_valeurs_autorisees = [0 for i in range(len(valeurs_autorisees))]
            
            index = var[0]*n+var[1]
            liste_voisins = [[(id-(id%n))//n, id%n] for id, estVoisin in enumerate(csp[index]) if estVoisin==1]
            for x_voisin, y_voisin in liste_voisins:     
                valeurs_autorisees_voisin = getValeursAutorisees([x_voisin, y_voisin])
                for val_voisin in valeurs_autorisees_voisin:
                    if val_voisin in valeurs_autorisees:
                        compteur_valeurs_autorisees[valeurs_autorisees.index(val_voisin)]+=1
            valeurs_autorisees_triee, compteur_trie =zip(*sorted(zip(valeurs_autorisees, compteur_valeurs_autorisees)))
        
            return valeurs_autorisees_triee
            
        def recursiveBacktracking():
            if(grilleComplete()):
                return (grille)
            var = selectionnerVariableNonAssignee()
            valeursAutorisees = getValeursAutoriseesLCV(var)

            for value in valeursAutorisees:
                grille[var[0]][var[1]]=value       
                result = recursiveBacktracking()
                if(result!=-1):
                    return result
                grille[var[0]][var[1]]=0
                
            return -1

        grille=self.grille.grille
        csp = self.grille.matriceAdjacenceGrapheContrainte
        n=self.grille.n

        return recursiveBacktracking()