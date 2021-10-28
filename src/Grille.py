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


grille = Grille()
path =r"C:\Users\Cyril\Documents\Cours UQAC\IA\TP2\git\TP2_IA\sudokus\sudoku1.txt"
grille.ImportSudoku(path)
grille.backtrackingSearch()
grille.afficherGrille()


