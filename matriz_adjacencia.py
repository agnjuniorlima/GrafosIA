class Grafo:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1 #trocar = por += se for grafo multiplo
        
        # se for grafo direcionado
        #self.grafo[v-1][u-1] = 1

    
    def mostra_matriz(self):
        print('A matriz de adjacencia é: ')

        for i in range(self.vertices):
            print(self.grafo[i])

g = Grafo(8)

g.add_aresta(1,2)
g.add_aresta(3,4)
g.add_aresta(2,3)

g.mostra_matriz()