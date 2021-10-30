import time, os


class Grille:
    def __init__(self, name, n=9):
        self.n=n
        self.matriceAdjacenceGrapheContrainte = self.creerMatriceAdjacenceGrapheContrainte()
        self.grille = self.importSudoku(name)
        
    def memeLigne(self,coordA, coordB):
        return coordA[0]==coordB[0]
    def memeColonne(self,coordA, coordB):
        return coordA[1]==coordB[1]
    def memeBloc(self,coordA, coordB):
        return (coordA[0]//3==coordB[0]//3 and coordA[1]//3==coordB[1]//3)

    def creerMatriceAdjacenceGrapheContrainte(self):
        n=self.n
        matriceAdjacenceGrapheContrainte = [[0 for i in range(n**2)] for i in range(n**2)]
        for i in range(n):
            for j in range(n):
                index=n*i+j
                for i1 in range(n):
                    for j1 in range(n):
                        coordA=[i,j]
                        coordB=[i1,j1]
                        index1=n*i1+j1
                        if((self.memeLigne(coordA,coordB) or self.memeColonne(coordA,coordB) or self.memeBloc(coordA,coordB)) and coordA!=coordB):
                           matriceAdjacenceGrapheContrainte[index][index1]=1
        return matriceAdjacenceGrapheContrainte

    def afficherGrille(self):
        n=self.n
        grille=self.grille
        for i in range(n):
            ligne="|"
            for j in range(n):
                ligne+=str(grille[i][j])+"|"
            print(ligne)

    def importSudoku(self, name):
        grid = list()
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "../sudokus/{}.txt".format(name)
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path) as f:
            for line in f:
                temp = [0 if x=="_" else int(x) for x in line.strip().split(" ") if x!=""]
                if(len(temp)!=0):
                    grid.append(temp)
        return grid

    

if __name__ == '__main__':
    
    grille = Grille("sudoku2")
    
    # path =r"C:\Users\robin\OneDrive - ESME\Cours\ESME\5eme année\IA\TP\TP2\sudokus\sudoku2.txt"
    # grille.importSudoku(path)
    # grille.afficherGrille()
    # print("\n")
    # start= time.time()
    # grille.backtrackingSearch()
    # end = time.time()
    # temps1=end-start
    # print(temps1," secondes")
    # grille.afficherGrille()
    # print("############")
    # grille.importSudoku(path)
    # grille.afficherGrille()
    # print("\n")
    # start = time.time()
    # grille.backtrackingSearchMRV()
    # end=time.time()
    # temps2=end-start
    # print(temps2," secondes")
    # rapport = 100-int(temps2/temps1*100)
    # print("Rédution du temps de ", rapport," %")
    # grille.afficherGrille()

