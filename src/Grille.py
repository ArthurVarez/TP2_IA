import os.path, random


class Grille:
    def __init__(self, name="", n=9):
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
            ligne="| "
            if((i)%3==0):
                print("-"*(self.n+self.n//3))
            for j in range(n):
                ligne+=str(grille[i][j])
                if((j+1)%3==0 and j!=0):
                    ligne+=" | "
            print(ligne)

    def importSudoku(self, name):
        script_dir = os.path.dirname(__file__)
        sudokus_folder = os.path.join(script_dir, "../sudokus/")
        if name=="":
            name = random.choice(os.listdir(sudokus_folder))
            print(name)
        else:
            name+=".txt"
        grid = list()
        #print(random.choice(os.listdir(r"C:\Users\robin\OneDrive - ESME\Cours\ESME\5eme année\IA\TP\TP2\git\TP2_IA\sudokus")))
        sudoku_file = sudokus_folder+name
        #abs_file_path = os.path.join(script_dir, rel_path)
        with open(sudoku_file) as f:
            for line in f:
                temp = [0 if x=="_" else int(x) for x in line.strip().split(" ") if x!=""]
                if(len(temp)!=0):
                    grid.append(temp)
        return grid

    

if __name__ == '__main__':
    
    grille = Grille("sudoku2")
    


