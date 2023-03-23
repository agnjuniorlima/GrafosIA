# eureliano = se o grafo não tiver nenhum vertice com o grau impar, ele vai ser eureliano começa e termina no mesmo vertice
# semi eureliano = grafo com dois vertices com grau impar que começa e termina em vertices diferentes

# grau é quantas arestas insidem no vertice

class Grafo:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def add_aresta(self, u, v):
        #grafo não direcionados
        self.grafo[u-1][v-1] += 1 #soma as arestas
        
        if u != v:
            self.grafo[v-1][u-1] +=1

    def mostrar_matriz(self):
        print('A matriz de adjacncias é: ')
        for i in range(self.vertices):
            print(self.grafo[i])

    def tem_aresta(self, u, v):
        if self.grafo[u-1][v-1] == 0:
            print(f'Não tem aresta entre os vertices {u} e {v}')
        else:
            print(f'Existe {self.grafo[u-1][v-1]} de arestas entre os vertices {u} e {v}')

    def eureliano(self):
        contador = 0

        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                if i == j:
                    grau = grau + 2 * self.grafo[i][j]
                else:
                    grau += self.grafo[i][j]
                
            if grau % 2 != 0:
                contador += 1
        if contador == 0:
            print('É um grafo Eureliano!')
        elif contador == 2:
            print(f'É um grafo semieureliano!')
        
        else:
            print('o grafo não é eureliano e nem semieureliano!')
        
    
g = Grafo(4)

g.add_aresta(1,2)
g.add_aresta(3,4)
#g.add_aresta(2,3)
#g.add_aresta(1,4)

g.eureliano()

g.mostrar_matriz()
