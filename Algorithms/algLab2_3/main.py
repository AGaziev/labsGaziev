def initGraph():
    nodeAmount = int(input("Enter amount of nodes: "))
    graph = {}
    for numberNode in range(1, nodeAmount + 1):
        nodeDest = input("Enter which nodes will connect node №{number}: ".format(number=numberNode))
        graph.update({'{key}'.format(key=numberNode): sorted(nodeDest.split())})
    return graph


def getAllComponents(graph, visited, order=None):
    components = []
    if not order:  # если порядок не установлен, то идем просто с меньшего
        order = graph.keys()
    for node in order:  # идем по заданному порядку
        if node not in visited:  # если не посещена
            components.append(dfs(graph, node, visited, component=[]))  # ищем компоненту связности с этой вершиной
    return components


times = []


def dfs(graph, node, visited, component):  # поиск в глубину
    if node not in visited:
        component.append(node)
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited, component)
    return component


def getAllStrong(graph, visited):
    for node in graph.keys():
        if node not in visited:
            dfs_with_time(graph, node, visited, 'start')
    order = times[::-1]  # переворачиваем счетчик прохода и определяем как порядок для поиска в глубину
    print('Sorted time order for Algorithm Kosaraju:', order)
    explored = []
    return getAllComponents(invertGraph(graph), explored, order)
    # получаем компоненты сильной связности через инвертированный граф с помощью поиска в глубину


def dfs_with_time(graph, node, visited, parent):
    global times  # счетчик прохода
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs_with_time(graph, n, visited, node)
        times.append(node)
    return times


def invertGraph(graph): # инвертирование графа
    invGraph = {str(i): [] for i in range(1, len(graph) + 1)}
    for node in graph:
        for connection in graph[node]:
            invGraph[connection].append(node)
            sorted(invGraph[connection])
    return invGraph


def main():
    graph = {'1': ['2', '5'], '2': ['3'], '3': ['4'], '4': ['2'], '5': ['4'], '6': ['7'], '7': ['6']}
    print('Graph:\n', graph)
    print('Inverted graph:\n', invertGraph(graph))

    visited = []  # посещенные вершины

    print('If nonoriented graph components:')
    components = getAllComponents(graph, visited)
    print(components)  # компоненты в неориентированном графе

    visited = []
    print('If oriented graph strongly connected components:\n{strongs}'.format(strongs=getAllStrong(graph, visited)))


if __name__ == '__main__':
    main()
