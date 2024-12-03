"""A function to find a connected components in graph"""

def find_conn_comp(graph, is_oriented: bool):
    """
    Finds all connected components in an undirected graph.

    A connected component is a subset of the vertices in a graph such that:
    - Any two vertices in the component are connected by a path.
    - No vertex in the component is connected to a vertex outside the component.

    Parameters:
        graph (dict): An adjacency list representation of the graph. 
                      Keys are vertices, and values are lists of adjacent vertices.

    Returns:
        list[list[int]]: A list of connected components. 
                         Each component is represented as a list of vertices.

    Example:
        >>> graph = {
        ...     0: [1, 2],
        ...     1: [0],
        ...     2: [0],
        ...     3: [4],
        ...     4: [3],
        ...     5: []
        ... }
        >>> find_conn_comp(graph, 0)
        [[0, 1, 2], [3, 4], [5]]
        
        >>> graph = {
        ...     0: [1, 2, 8],
        ...     1: [0, 2],
        ...     2: [0, 1, 8],
        ...     3: [],
        ...     4: [5],
        ...     5: [4, 6],
        ...     6: [5, 7],
        ...     7: [6],
        ...     8: [0, 2]
        ... }
        >>> find_conn_comp(graph, 0)
        [[0, 1, 2, 8], [3], [4, 5, 6, 7]]
    """
    if is_oriented:
        raise ValueError("The graph is oriented. Searching for connected components is not possible.")

    visited = {v:0 for v in graph}
    all_components = []

    def dfs(v, component):
        """
        Performs a depth-first search (DFS) starting from vertex v, 
        adding all visited vertices to the connected component.
        """
        visited[v] = True
        component.append(v)
        for neighbor in graph:
            if neighbor in graph[v] and not visited[neighbor]:
                dfs(neighbor, component)

    for v in graph:
        if not visited[v]:
            component = []
            dfs(v, component)
            all_components.append(component)

    return all_components

# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())
