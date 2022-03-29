import math


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for i in range(vertex)] for i in range(vertex)]
        # print(self.graph)

    def printWays(self, parents, weightOfPaths):
        for i in range(self.V):
            print(f"Way to {i}", end=": ")
            parent = i
            while parents[parent] != parent:
                print(f"{parent}<-", end="")
                parent = parents[parent]
            print(parent, f"in {weightOfPaths[i]}")

    def getMinimalFromRemaining(self, weights, out):
        nextW = math.inf # вес до след вершины
        nextI = -1 # номер следующей вершины
        for i in range(self.V):
            if i not in out and nextW > weights[i]:
                nextW = weights[i]
                nextI = i
        return nextI

    def Dijkstra(self, start=0):
        out = [start]  # уже "побывавшие" в очереди вершины
        weightPath = [math.inf] * self.V  # массив с весами вершин
        weightPath[start] = 0
        parent = [0 for i in range(self.V)]  # храним родителей для вывода пути
        queue = [start]
        while len(out) < self.V:
            row = queue.pop(0)  # получаем первый из очереди
            for i in range(self.V):
                if self.graph[row][i] != 0 and i not in out:  # если есть путь и конечная вершина не "побывавшая"
                    if weightPath[row] + self.graph[row][i] < weightPath[i]:  # если есть смысл менять
                        parent[i] = row  # изменяем родителя
                        weightPath[i] = weightPath[row] + self.graph[row][i]
            nextRow = self.getMinimalFromRemaining(weightPath,
                                                   out)  # поиск следующего индекса для очереди (минимального)
            queue.insert(0, nextRow)
            out.append(nextRow)
            print(out, weightPath, parent)
        self.printWays(parent, weightPath)

    def BellmanFord(self, start=0):
        dist = [math.inf] * self.V
        dist[start] = 0
        for i in range(self.V - 1):
            for u in range(self.V):
                for v in range(self.V):
                    if self.graph[u][v] != 0:
                        if dist[u] != math.inf and dist[u] + self.graph[u][v] < dist[v]:
                            dist[v] = dist[u] + self.graph[u][v]

        print(dist)


def graphInit(g, gm=None):
    if not gm:
        for i in range(g.V):
            while True:
                try:
                    gm.append(list(input("Введите стартовую вершину, конечную и вес: ").split()))
                except Exception as e:
                    if "y" == input("Неправильный ввод, следующая вершина? y/n: "):
                        continue
        for u, v, w in gm:
            g.graph[u][v] = w
        gm.clear()
    else:
        for i in range(g.V):
            for j in range(g.V):
                if gm[i][j] != 0:
                    g.graph[i][j] = gm[i][j]
    return g


def main():
    g = Graph(6)
    gMat1 = [[0, 7, 9, 0, 0, 14],
             [7, 0, 10, 15, 0, 0],
             [9, 10, 0, 11, 0, 2],
             [0, 15, 11, 0, 6, 0],
             [0, 0, 0, 6, 0, 9],
             [14, 0, 2, 0, 9, 0]]
    gMat2 = [[0, 3, 1, 3, 0, 0],
             [3, 0, 4, 0, 0, 0],
             [1, 4, 0, 0, 7, 5],
             [3, 0, 0, 0, 0, 2],
             [0, 0, 7, 0, 0, 4],
             [0, 0, 5, 2, 4, 0]]
    g = graphInit(g, gMat2)
    g.Dijkstra()
    g.BellmanFord()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
