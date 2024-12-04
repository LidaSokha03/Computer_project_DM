"""
This module is a part of the whole computer project from discrete mathematics.
"""

from copy import deepcopy


def dfs(graph, node, visited):
    """
    The function of the algorithm called DFS (Depth-First Search) that tries to visit all
    the points that are connected with another points in order to find out whether the graph
    is connected or not.
    """
    visited.append(node)
    neighbours = graph[node]
    for neighbour in neighbours:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


def find_points(graph, is_oriented: bool):
    """
    Finds the connection points in an undirected graph.
    Returns the list of such points.

    >>> graph = {\
    1: [2, 4],\
    2: [1, 3, 5],\
    3: [2, 6],\
    4: [1, 7],\
    5: [2, 8],\
    6: [3],\
    7: [4, 8],\
    8: [5, 7]\
    }
    >>> find_points(graph, is_oriented=False)
    [2, 3]
    """
    if is_oriented is True:
        raise ValueError("This function only works with undirected graphs, not oriented ones.")
    connection_points = []
    for key in graph:
        copied_graph = deepcopy(graph)
        visited = []
        copied_graph.pop(key)
        for other_points in copied_graph:
            if key in copied_graph[other_points]:
                copied_graph[other_points].remove(key)
        any_point = next(iter(copied_graph))
        dfs(copied_graph, any_point, visited)
        if len(visited) != len(copied_graph):
            connection_points.append(key)
    return connection_points


def bridges(graph, is_oriented: bool):
    """
    Find all bridges in an undirected graph.
    Returns a list of tuples of bridges.
    >>> bridges({'1': ['5', '3'], '5': ['1', '4'], '6': ['4'],\
 '4': ['6', '5'], '3': ['1'], '2': ['7'], '7': ['2']}, False)
    [('4', '6'), ('5', '4'), ('1', '5'), ('1', '3'), ('2', '7')]
    >>> bridges({0: [1, 2], 1: [0, 2, 3, 4, 6], 2: [0, 1], 3:\
 [1, 5], 4: [1, 5], 5: [3 ,4], 6: [1]}, False)
    [(1, 6)]
    """
    if is_oriented:
        raise ValueError('The graph is oriented.')

    bridges_list = []

    def dfs_func(node_new, node_old, way_length):
        '''
        Function of DFS algorithm that visits all nodes in graph.
        '''
        visited[node_new] = True
        first_visit_way[node_new] = way_length
        minimum_way[node_new] = way_length
        way_length += 1


        for connected_node in graph.get(node_new):
            if not visited[connected_node]:
                dfs_func(connected_node, node_new, way_length)

                minimum_way[node_new] = min(minimum_way[node_new], minimum_way[connected_node])

                if minimum_way[connected_node] > first_visit_way[node_new]:
                    bridges_list.append((node_new, connected_node))
            elif connected_node != node_old:
                minimum_way[node_new] = min(minimum_way[node_new], first_visit_way[connected_node])


    way_length = 0
    visited = {}
    first_visit_way = {}
    minimum_way = {}
    for node in graph:
        visited[node] = False
        first_visit_way[node] = 0
        minimum_way[node] = 0

    for node in graph:
        if not visited[node]:
            dfs_func(node, None, way_length)

    return bridges_list
