class Graph:
    eulerianGraph = []

    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for i in range(vertex)] for i in range(vertex)]
        self.cycle = []  # эйлеров цикл
        self.edgeNum = 0  # количество вершин
        self.visited = []  # вершины посещяемые во время обхода

    def findEulerianCycle(self, start):
        cycleSize = self.edgeNum / 2  # в неориентированном простом графе количество ребер

        self.eulerianGraph = self.graph  # отдельный граф для сохранения исходных данных
        self.visited.append(start)  # добавляем начало в список посещенных
        self.modifiedDfs(start, start)  # первый проход для поиска первого Эйлерова пути

        while len(self.cycle) < cycleSize:
            print(self.visited)
            self.cycle.append(self.visited[-1])  # "вытаскиваем" из посещенных последний
            del self.visited[-1]
            self.modifiedDfs(self.visited[-1],
                             self.visited[-1])
        self.cycle.append(start)

    def modifiedDfs(self, v, startPoint):
        for i, connected in enumerate(self.eulerianGraph[v]):  # находим первый не посещенный выход(ребро) из вершины
            if connected:
                if i == startPoint:
                    self.visited.append(i)  # добавляем конец в список
                    self.deleteEulEdge(v, i)  # удаляем ребро по которому пройдем
                    return  # выходим если пришли к началу
                self.visited.append(i)  # добавляем в список посещенных
                self.deleteEulEdge(v, i)  # удаляем ребро по которому пройдем
                self.modifiedDfs(i, startPoint)  # рекурсивно запускаем проход по циклу дальше
                return  # выходим так как не требуется полный проход в глубину

    def deleteEulEdge(self, s, e):  # удаление ребра
        self.eulerianGraph[s][e] = 0
        self.eulerianGraph[e][s] = 0


def graphInit(g, gm):
    for i in range(g.V):
        for j in range(g.V):
            if gm[i][j] != 0:
                g.edgeNum += 1
                g.graph[i][j] = 1
                g.graph[j][i] = 1
    return g


gMat = [
    [0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0],
]
gMat2 = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
]
g = Graph(7)
g = graphInit(g, gMat)
for i in g.graph:
    print(i)
g.findEulerianCycle(0)
print(g.cycle)
