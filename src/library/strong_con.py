'''A function for finding strongly connected components in a directed graph'''


def kosaraju_scc(graph, is_oriented: bool):
    """
    Finds strongly connected components (SCC) of a directed graph.

    :param graph: dict, A dictionary representing a graph in the form of an adjacency list.
                        Keys are vertices, values ​​are a list of neighboring vertices.
    :param is_oriented: bool, True if graph is oriented, False if not

    :return: list[list[int]], List of components of strong connectivity. 
    Each component is represented as a list of vertices.
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
    A function for depth-first graph traversal (DFS).
    Adds vertices to the stack in order of completion.

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
    Creates an inverted graph (changes the direction of all edges).

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
    A function for finding components of strong connectivity
    in the inverse graph.

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
