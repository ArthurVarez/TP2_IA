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



