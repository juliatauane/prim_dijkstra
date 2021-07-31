import time
start_time = time.time()

class Node:
    def __init__(self, arg_id) :
        self._id = arg_id

class Grafo:
    def __init__(self, arg_source, arg_adj_lista) :
        self.source = arg_source
        self.adjlista = arg_adj_lista

    def Prim(self):
        Fila_prioridade = { Node(self.source) : 0 }
        added = [False] * len(self.adjlista)
        mstprim = 0

        while Fila_prioridade :
            node = min (Fila_prioridade, key=Fila_prioridade.get)
            custo = Fila_prioridade[node]

            del Fila_prioridade[node]
            if added[node._id] == False :
                mstprim += custo
                added[node._id] = True
                print("Added Node: " + str(node._id) + ", custo agora:"+str(mstprim))

                for item in self.adjlista[node._id] :
                    adjnode = item[0]
                    adjcusto = item[1]

                    if added[adjnode] == False :
                        Fila_prioridade[Node(adjnode)] = adjcusto
        return mstprim

def main() :
    g_vertice = {}
    g_vertice [0] = [ (0,0), (1,15), (2,25), (3,36)]
    g_vertice [1] = [ (0,0), (1,11), (2,22), (3,33)]
    g_vertice [2] = [ (0,0), (1,12), (2,23), (3,34)]
    g_vertice [3] = [ (0,0), (1,13), (2,24), (3,35)]
    g = Grafo(0, g_vertice )
    custo = g.Prim()
    print("Árvore de Amplitude Mínima:" + str(custo) +"\n")
if __name__ == "__main__" :
    main()
    end_time= time.time()
    tempo= (end_time - start_time)
    print("tempo de execução:", tempo)