'''Функція для пошуку компонентів сильної зв'язності в орієнтованому графі'''

graph_ = {
    0: [2],
    1: [0,3],
    2: [1, 3, 4],
    3: [5],
    4: [5, 6],
    5: [3],
    6: [4,7],
    7: [5,6]}

def kosaraju_scc(graph, is_oriented: bool):
    """
    Знаходить компоненти сильної зв'язності (SCC) орієнтованого графа.

    :param graph: dict, Словник, що представляє граф у вигляді списку суміжності.
                      Ключі — вершини, значення — список сусідніх вершин.

    
    :return: list[list[int]], Список компонент сильної зв'язності. 
                         Кожна компонента представлена як список вершин.
    >>> kosaraju_scc(graph_)
    [[0, 1, 2], [4, 6, 7], [3, 5]]
    """
    if not is_oriented:
        return -1
    #1)
    visited = {v: False for v in graph}
    stack = []
    for v in graph:
        if not visited[v]:
            dfs(v, visited, stack,graph)

    #2)
    transposed_graph = transpose_graph(graph)
    #3)
    visited = {v: False for v in graph}
    scc_list = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_scc(v, visited, component, transposed_graph)
            scc_list.append(component)

    return scc_list


def dfs(vertex, visited, stack,graph):
    """
    Функція для обходу графа у глибину (DFS).
    Додає вершини в стек у порядку завершення обробки.

    :param vertex: int, Current vertex.
    :param visited: dict, Dictionary, that that contains the information if vertex is visited.
    :param stack: list, Stack that saves the order of completing of processing.
    """
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack, graph)
    stack.append(vertex)





def transpose_graph(graph):
    """
    Створює обернений граф (змінює напрямок усіх ребер).

    :param graph: dict, Original graph.
    :return: dict, Transpone graph.
    """
    transposed_graph = {v: [] for v in graph}
    for v in graph:
        for neighbor_v in graph[v]:
            transposed_graph[neighbor_v].append(v)
    return transposed_graph






def dfs_scc(vertex, visited, component, transposed_graph):
    """
    Функція для пошуку компонент сильної зв'язності
    у оберненому графі.

    :param vertex: int, Current vertex.
    :param visited: dict, Dictionary, that that contains the information if vertex is visited.
    :param component: list, List of vertexes in current component.
    :param transposed_graph: dict, Transpone graph.
    """
    visited[vertex] = True
    component.append(vertex)
    for neighbor in transposed_graph[vertex]:
        if not visited[neighbor]:
            dfs_scc(neighbor, visited, component, transposed_graph)
