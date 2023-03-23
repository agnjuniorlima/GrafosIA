class Grafo:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def add_aresta(self, u, v, peso):
        #para grafo direcionado
        self.grafo[u-1].append([v, peso])

        #se grafo não for direcionado
        #self.grafo[v-1].append([u, peso])
    
    def mostrar_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end=' ')
            for j in self.grafo[i]:
                print(f'{j} ->', end=' ')
            print('')

g = Grafo(4)

g.add_aresta(1, 2, 5)
g.add_aresta(1, 3, 7)
g.add_aresta(1, 4, 6)
g.add_aresta(2, 3, 9)

g.mostrar_lista()