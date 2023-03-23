class Grafo:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def add_aresta(self, u, v):
        #para grafo direcionado
        self.grafo[u-1].append(v)

        #se grafo não for direcionado
        #self.grafo[v-1].append(u)
    
    def mostrar_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end=' ')
            for j in self.grafo[i]:
                print(f'{j} ->', end=' ')
            print('')

g = Grafo(4)

g.add_aresta(1,2)
g.add_aresta(1,3)
g.add_aresta(1,4)
g.add_aresta(2,3)

g.mostrar_lista()