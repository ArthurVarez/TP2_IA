import time
import math
class Grille:
    def __init__(self,n=9):
        self.n=n
        self.creerMatriceAdjacenceGrapheContrainte()
    def memeLigne(self,coordA, coordB):
        return coordA[0]==coordB[0]
    def memeColonne(self,coordA, coordB):
        return coordA[1]==coordB[1]
    def memeBloc(self,coordA, coordB):
        return (coordA[0]//3==coordB[0]//3 and coordA[1]//3==coordB[1]//3)

    def creerMatriceAdjacenceGrapheContrainte(self):
        n=self.n
        self.matriceAdjacenceGrapheContrainte = [[0 for i in range(n**2)] for i in range(n**2)]
        for i in range(n):
            for j in range(n):
                index=n*i+j
                for i1 in range(n):
                    for j1 in range(n):
                        coordA=[i,j]
                        coordB=[i1,j1]
                        index1=n*i1+j1
                        if((self.memeLigne(coordA,coordB) or self.memeColonne(coordA,coordB) or self.memeBloc(coordA,coordB)) and coordA!=coordB):
                           self.matriceAdjacenceGrapheContrainte[index][index1]=1

    def afficherGrille(self):
        n=self.n
        grille=self.grille
        for i in range(n):
            ligne="|"
            for j in range(n):
                ligne+=str(grille[i][j])+"|"
            print(ligne)

    def ImportSudoku(self,path):
        grid = list()
        with open(path) as f:
            for line in f:
                temp = [0 if x=="_" else int(x) for x in line.strip().split(" ") if x!=""]
                if(len(temp)!=0):
                    grid.append(temp)
        self.grille = grid

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
            orderDomainValues = [i for i in range(1,n+1)]
            for value in orderDomainValues:
                if(value in valeursAutorisees):
                    grille[var[0]][var[1]]=value
                    result = recursiveBacktracking(grille)
                    if(result!=-1):
                        return result
                    grille[var[0]][var[1]]=0
            return -1
        grille=self.grille
        csp = self.matriceAdjacenceGrapheContrainte
        n=self.n
        return recursiveBacktracking(grille)

    def backtrackingSearchMRV(self):
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
        def grilleComplete(grille):
            for i in range(n):
                for j in range(n):
                    if(grille[i][j]==0):
                        return False
            return True

        def setValeursAutorisees(var, grille, csp):
            index = var[0]*n+var[1]
            possibilites = [1,2,3,4,5,6,7,8,9]
            for index1 in range(n**2):
                j=index1%n
                i=(index1-j)//n
                if(csp[index][index1]==1 and (grille[i][j] in possibilites)):
                    possibilites.remove(grille[i][j])
            return possibilites

        def selectionnerVariableNonAssignee(grille,csp):
            nBValeurLegales=math.inf
            var=[0,0]
            for i in range(n):
                for j in range(n):
                    possibilites = matricePossibilites[i][j]
                    if(grille[i][j]==0 and len(possibilites)<nBValeurLegales):
                        nBValeurLegales = len(possibilites)
                        var=[i,j]
            return var

        def recursiveBacktracking(grille,csp,matricePossibilites):
            if(grilleComplete(grille)):
                return grille
            var = selectionnerVariableNonAssignee(grille,csp)
            valeursAutorisees = matricePossibilites[var[0]][var[1]]
            orderDomainValues = [i for i in range(1,n+1)]
            for value in orderDomainValues:
                if(value in valeursAutorisees):
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
        grille=self.grille
        n=self.n
        csp = self.matriceAdjacenceGrapheContrainte
        matricePossibilites = setMatricePossibilites(grille,csp)
        return recursiveBacktracking(grille,csp, matricePossibilites)

grille = Grille()
path =r"C:\Users\Cyril\Documents\Cours UQAC\IA\TP2\git\TP2_IA\sudokus\sudoku2.txt"
grille.ImportSudoku(path)
grille.afficherGrille()
print("\n")
start= time.time()
grille.backtrackingSearch()
end = time.time()
temps1=end-start
print(temps1," secondes")
grille.afficherGrille()
print("############")
grille.ImportSudoku(path)
grille.afficherGrille()
print("\n")
start = time.time()
grille.backtrackingSearchMRV()
end=time.time()
temps2=end-start
print(temps2," secondes")
rapport = 100-int(temps2/temps1*100)
print("Rédution du temps de ", rapport," %")
grille.afficherGrille()

