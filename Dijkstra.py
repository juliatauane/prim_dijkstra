import math
import random
import time
start_time = time.time()

class HeapMin:

    def __init__(self):
        self.nos = 0
        self.heap = []

    def adiciona_no(self, u, indice):
        self.heap.append([u, indice])
        self.nos += 1
        f = self.nos
        while True:
            if f == 1:
                break
            p = f // 2
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                f = p

    def mostra_heap(self):
        print('A estrutura heap é a seguinte:')
        n = int(math.log(self.nos, 2))
        a = 0
        for i in range(n):
            for j in range(2 ** i):
                print(f'{self.heap[a]}', end='  ')
                a += 1
            print('')
        for i in range(self.nos-a):
            print(f'{self.heap[a]}', end='  ')
            a += 1
        print('')

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f-1][0]:
                    f += 1
            if self.heap[p-1][0] <= self.heap[f-1][0]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]
                p = f
        return x

    def tamanho(self):
        return self.nos

    def menor_elemento(self):
        if self.nos != 0:
            return self.heap[0]
        return 'A árvore está vazia'

    def filhoesquerda(self, u):
        if self.nos >= 2*u:
            return self.heap[2*u-1]
        return 'Esse nó não tem filho'

    def filhodireita(self, u):
        if self.nos >= 2*u+1:
            return self.heap[2*u]
        return 'Esse nó não tem filho da direita'

    def pai(self, u):
        return self.heap[u // 2]

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo = [[-1, 0] for i in range(self.vertices)]
        custo[origem - 1] = [0, origem]
        h = HeapMin()
        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if custo[i][0] == -1 or custo[i][0] > dist + self.grafo[v-1][i]:
                        custo[i] = [dist + self.grafo[v-1][i], v]
                        h.adiciona_no(dist + self.grafo[v-1][i], i+1)
        return custo

g = Grafo(4)

#self.grafo(u,v,peso)
#u=
#v:

g.adiciona_aresta(1, 2, 70)
g.adiciona_aresta(2, 1, 50)
g.adiciona_aresta(1, 2, 18)
g.adiciona_aresta(2, 1, 13)

g.mostra_matriz()

resultado_dijkstra = g.dijkstra(1)
print("Caminho mínimo:", resultado_dijkstra)

end_time= time.time()
tempo= end_time - start_time
print("tempo de execução:", tempo)
