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
            for i in range(n):
                for j in range(n):
                    if(grille[i][j]==0):
                        return False
            return True

        def selectionnerVariableNonAssignee(grille):
            for i in range(n):
                for j in range(n):
                    if(grille[i][j]==0):
                        return [i,j]

        def setValeursAutorisees(var, grille, csp):
            index = var[0]*n+var[1]
            possibilites = [1,2,3,4,5,6,7,8,9]
            for index1 in range(n**2):
                j=index1%n
                i=(index1-j)//n
                if(csp[index][index1]==1 and (grille[i][j] in possibilites)):
                    possibilites.remove(grille[i][j])
            return possibilites

        def recursiveBacktracking(grille):
            if(grilleComplete(grille)):
                return grille
            var = selectionnerVariableNonAssignee(grille)
            valeursAutorisees = setValeursAutorisees(var, grille, csp)
            for value in valeursAutorisees:
                grille[var[0]][var[1]]=value
                result = recursiveBacktracking(grille)
                if(result!=-1):
                    return result
                grille[var[0]][var[1]]=0
            return -1
        
        grille=self.grille.grille
        csp = self.grille.matriceAdjacenceGrapheContrainte
        n=self.grille.n
        return recursiveBacktracking(grille)

    def backtrackingSearchMRV_LCV(self):
        def grilleComplete(grille):
            for i in range(n):
                for j in range(n):
                    if(grille[i][j]==0):
                        return False
            return True
        def setMatricePossibilites(grille,csp):
            matricePossibilites = [[[] for i in range(n)] for j in range(n)]
            for i in range(n):
                for j in range(n):
                    if(grille[i][j]==0):
                        matricePossibilites[i][j]=setValeursAutorisees([i,j], grille, csp)
                    else:
                        matricePossibilites[i][j]=[]
            return matricePossibilites
        def deleteMatricePossibilites(matricePossibilites, var, value, csp):
            index=var[0]*n+var[1]
            for index1 in range(n**2):
                if(csp[index][index1]):
                    j=index1%n
                    i=(index1-j)//n
                    if(value in matricePossibilites[i][j]):
                        matricePossibilites[i][j].remove(value)

        def addMatricePossibilites(matricePossibilites, var, value, csp):
            index=var[0]*n+var[1]
            for index1 in range(n**2):
                if(csp[index][index1]):
                    j=index1%n
                    i=(index1-j)//n
                    if(value not in matricePossibilites[i][j]):
                        matricePossibilites[i][j].append(value)

        

        def selectionnerVariableNonAssignee(grille):
            nBValeurLegales=math.inf
            var=[0,0]
            for i in range(n):
                for j in range(n):
                    possibilites = matricePossibilites[i][j]
                    if(grille[i][j]==0 and len(possibilites)<nBValeurLegales):
                        nBValeurLegales = len(possibilites)
                        var=[i,j]
            return var

        def setValeursAutorisees(var, grille, csp):
            index = var[0]*n+var[1]
            possibilites = [1,2,3,4,5,6,7,8,9]
            for index1 in range(n**2):
                j=index1%n
                i=(index1-j)//n
                if(csp[index][index1]==1 and (grille[i][j] in possibilites)):
                    possibilites.remove(grille[i][j])
            return possibilites

        def chooseBestValue(var, matrice_possibilite):
            valeurs_autorisees = matrice_possibilite[var[0]][var[1]]
            #if valeurs_autorisees==[]:
            #    return []
            compteur_valeurs_autorisees = [0 for i in range(len(valeurs_autorisees))]
            
            index = var[0]*n+var[1]
            liste_voisins = [id for id, estVoisin in enumerate(csp[index]) if estVoisin==1]
            for index_voisin in liste_voisins:     
                x_voisin=index_voisin %n
                y_voisin=(index_voisin-x_voisin)//n
                valeurs_autorisees_voisin = matrice_possibilite[y_voisin][x_voisin]
                for val_voisin in valeurs_autorisees_voisin:
                    if val_voisin in valeurs_autorisees:
                        compteur_valeurs_autorisees[valeurs_autorisees.index(val_voisin)]+=1
            valeurs_autorisees_triee, compteur_trie =zip(*sorted(zip(valeurs_autorisees, compteur_valeurs_autorisees)))
        
            return valeurs_autorisees_triee[0]
            #return valeurs_autorisees_triee

        def recursiveBacktracking(grille,csp, matricePossibilites):
            if(grilleComplete(grille)):
                return (grille, matricePossibilites)
            var = selectionnerVariableNonAssignee(grille)

            valeursAutorisees = matricePossibilites[var[0]][var[1]]
            #valeursAutorisees = chooseBestValue(var, matricePossibilites)
            
            for i in range(len(valeursAutorisees)):
                value = chooseBestValue(var, matricePossibilites)
            #for value in valeursAutorisees:
                grille[var[0]][var[1]]=value
                matricePossibilites[var[0]][var[1]].remove(value)
                deleteMatricePossibilites(matricePossibilites,var,value,csp)
                result = recursiveBacktracking(grille,csp, matricePossibilites)
                if(result!=-1):
                    return result
                grille[var[0]][var[1]]=0
                matricePossibilites[var[0]][var[1]].append(value)
                addMatricePossibilites(matricePossibilites,var,value,csp)
            return -1

        grille=self.grille.grille
        csp = self.grille.matriceAdjacenceGrapheContrainte
        n=self.grille.n
        
        matricePossibilites = setMatricePossibilites(grille,csp)
        
        return recursiveBacktracking(grille,csp, matricePossibilites)[0]