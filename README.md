# Algoritmo de PRIM

O algoritmo de PRIM é um algoritmo que transforma um dado grafo conectado, não
orientado e ponderado (com pesos/custos) em uma árvore de amplitude mínima, ou seja,
uma árvore que minimize o peso/custo total. Portanto, através do subconjunto das arestas
desse grafo é formada uma árvore que inclui todos os vértices com a soma mínima de
todas as árvores que podem ser formadas a partir do gráfico.

Funcionamento:

O primeiro passo é a escolha de um vértice para ser a raiz da árvore, ou seja, o vértice
ponto de partida para se iniciar a busca das arestas, a partir desse vértice são analisados os
demais vértices que possuem o menor custo.
Desta forma é escolhida a aresta com menor custo e adicionada a lista de solução. Em
seguida, é eleito um vértice ainda não elencado com a aresta de menor custo e novamente
o caminho (aresta) é guardada na lista de solução. O processo é repetido para achar o
próximo vértice com aresta de menor custo, até encontrar o menor caminho para todos os
vértices.
Portanto, o algoritmo começa com uma subárvore contendo apenas o primeiro vértice e
vai expandindo essa subárvore, escolhendo sempre o vértice mais próximo que ainda não
faça parte da subárvore.

Complexidade de tempo:

A complexidade de tempo do algoritmo de Prim é da ordem de O (E log V).

#Algoritmo de Dijkstra

O algoritmo de Dijkstra é um algoritmo que encontra o caminho mais curto de um dado
grafo de única origem com pesos não negativos e dirigido. É utilizada a técnica de
relaxamento na qual para cada vértice no grafo é estimada a menor distância a partir da
origem. Ou seja, relaxar uma aresta significa testar se o caminho de um vértice ao outro a
aresta permite diminuir o valor da distância.

Funcionamento:

O algoritmo funciona em qualquer subcaminho, caminho mais curto de um vértice a outro.
O primeiro passo é escolher um vértice inicial, colocar os vértices em uma fila de
prioridade. Dessa forma, o processo sempre começa a busca pelo vértice na qual o caminho
desde o vértice de origem é o mais curto.
É feito o relaxamento das arestas, de forma a atualizar cada vértice com o peso da sua
aresta, ou seja, o comprimento/custo do seu caminho.
Portanto, a cada iteração é escolhido um vértice não visitado com o menor peso de aresta,
ou seja, menor caminho. O Processo é repetido até que todos os vértices tenham sidos
visitados.

Complexidade de tempo:

A complexidade de tempo do algoritmo de Dijkstra é da ordem de O (E log V), sendo E o
número de arestas e V o número de vértices.
Complexidade do espaço: O(V)
Desempenho do algoritmo pode ser melhorado utilizando um heap na implementação,
dessa forma seria da ordem de O (E + V log V).

# DIFERENÇA ENTRE ALGORITMO DE PRIM E DJKSTRA

Algoritmo de Prim: 
Constrói Árvore Geradora Mínima
Funciona para grafos não direcionados 
Funciona para arestas de pesos negativos 

Algoritmo de Dijkstra:
Árvore de Caminho Mais Curto
Funciona bem para grafos direcionados
Não funciona para arestas de pesos negativos

O algoritmo de Prim funciona de modo muito semelhante ao algoritmo de Dijkstra para
localizar caminhos mínimos em um grafo, porém o algoritmo de Dijkstra difere do de Prim
pois o algoritmo de Dijkstra pega o valor da aresta e joga como valor do vértice. O de Prim é
a distância a partir do nó inicial, é o custo daquele nó a partir do nó inicial.
Os algoritmos são semelhantes no sentido que ambos pdoem usar uma fila de prioridades
mínimas para encontrar o vértice com aresta de menor custo, no Algoritmo de Dijkstra a
lista de soluções, e no algoritmo de Prim a árvore de amplitude mínima. Ou seja, adicionam
esse vértice ao conjunto e ajustam os pesos dos vértices restantes fora do conjunto de
acordo com o resultado dessas operações.
As aplicações de cada algoritmo podem ser distintas, sendo o que o Prim aplicado para
colocação de cabos de uma fiação elétrica, por exemplo, de forma a calcular a melhor
forma de passar a fiação por todas as residências (representando os vértices) com um
custo mínimo (peso das arestas). Já o algoritmo de Dijkstra é utilizado para encontrar o
caminho mais curto, e pode ser aplicado para encontrar locais no mapa, por exemplo.
