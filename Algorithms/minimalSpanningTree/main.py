import math


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def applyUnion(self, parent, rank, x, y):
        xroot = self.search(parent, x)  # находим принадлежность компоненте вершины x
        yroot = self.search(parent, y)  # ... y
        print(x, y, xroot, yroot)
        if rank[xroot] < rank[yroot]:  # если x не принадлежит компоненте - связываем
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:  # если y не принадлежит компоненте - связываем
            parent[yroot] = xroot
        else:  # если обе не принадлежат ни одной компоненте или обе являются компонентами
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        print(self.graph)
        result = []
        i, e = 0, 0 #
        self.graph = sorted(self.graph, key=lambda item: item[2]) # сортировка по весу
        parent = []  # хранение ссылок на родителей
        rank = []  # хранение номера и значимости компоненты связности
        for node in range(self.V):  # создаем для каждой вершины свою компоненту связности
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)  # принадлежность к компоненте
            y = self.search(parent, v)
            if x != y:  # не в одной компоненте связности
                e = e + 1
                result.append([u, v, w])
                print(rank, parent, end=" ")
                self.applyUnion(parent, rank, x, y)
        print(rank, parent)
        for u, v, weight in result:
            print(f"Edge: {u}<->{v} for {weight}")

    def getMin(self, inTree):
        resEdge = (-1, -1, math.inf)
        for node in inTree:
            minEdge = (-1, -1, math.inf)  # если не найден минимальный по условию
            for i in self.graph:
                if ((i[0] == node or i[1] == node) and  # один из элементов в минимальном остовном дереве
                        (i[1] not in inTree or i[0] not in inTree) and  # а второй нет
                        minEdge[2] > i[2]):  # условие неубывания
                    minEdge = i
            if resEdge[2] > minEdge[2]:
                resEdge = minEdge
            print(f"min in {node}: ", minEdge)
        return resEdge

    def prim(self, start=0):
        self.add_edge(-1, -1, math.inf)
        print(self.graph)
        result = []  # массив с ребрами
        inTree = {start}  # массив уже используемых вершин
        while len(inTree) < self.V:
            minWay = self.getMin(inTree)
            print(minWay)
            if minWay[2] == math.inf:
                break
            result.append(minWay)
            inTree.add(minWay[0])
            inTree.add(minWay[1])
            print(inTree, result)
        for u, v, weight in result:
            print(f"Edge: {u}<->{v} for {weight}")


def graphInit(graph, gm=None):
    if not gm:
        for i in range(graph.V):
            while True:
                try:
                    gm.append(list(input("Введите стартовую вершину, конечную и вес: ").split()))
                except Exception as e:
                    if "y" == input("Неправильный ввод, следующая вершина? y/n: "):
                        continue
    for u, v, w in gm:
        graph.add_edge(u, v, w)
    return graph


g = Graph(6)
gmat = [[0, 1, 2],
        [0, 2, 1],
        [0, 3, 12],
        [0, 4, 2],
        [1, 3, 3],
        [1, 5, 5],
        [2, 4, 3],
        [3, 4, 4],
        [3, 5, 4]]
gmat2 = [[0, 2, 5],
         [3, 4, 7],
         [0, 1, 8],
         [1, 2, 9],
         [2, 4, 10],
         [1, 3, 11],
         [3, 5, 12]]
g = graphInit(g, gmat)
g.kruskal()
g.prim()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
