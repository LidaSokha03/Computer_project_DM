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
    >>> graph = {\
    1: [2],\
    2: [1, 3],\
    3: [2],\
    5: [6],\
    6: [5]\
    }
    >>> bridges(graph, is_oriented=False)
    [(1, 2), (2, 3), (5, 6)]
    """
    if is_oriented:
        raise ValueError('The graph is oriented.')

    bridges_list = []
    copied_graph = graph.copy()
    for edge in copied_graph:
        graph.pop(edge)

        for edge_value in copied_graph.get(edge):
            if edge_value in graph:
                pass
            else:
                if edge in copied_graph.get(edge_value):
                    tuple_add = (edge_value, edge)
                    bridges_list.append(tuple_add)
                else:
                    tuple_add = (edge, edge_value)
                    bridges_list.append(tuple_add)

    return bridges_list
