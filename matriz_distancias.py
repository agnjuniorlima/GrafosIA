class Grafo:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso #trocar = por += se for grafo multiplo
        
        # se for grafo direcionado
        #self.grafo[v-1][u-1] = 1

    
    def mostra_matriz(self):
        print('A matriz de adjacencia é: ')

        for i in range(self.vertices):
            print(self.grafo[i])



# g.add_aresta(1,2,5)
# g.add_aresta(3,4,9)
# g.add_aresta(2,3,3)
v = int(input('Digite a quantidade de vertices: '))
g = Grafo(v)

a = int(input('Digite a quantidade de arestas: '))
for i in range(a):
    u = int(input('Para qual vertice chega esta aresta? '))
    v = int(input('Para qual vertice chega a resta? '))
    p = int(input('Qual é o peso desta aresta? '))
    g.add_aresta(u, v, p)

g.mostra_matriz()