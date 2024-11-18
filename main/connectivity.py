def dfs(graph, v, component, visited, num_vertises):
    """
    Performs a depth-first search (DFS) starting from vertex v, 
    adding all visited vertices to the connected component.

    Parameters:
    v : int
        The starting vertex for the DFS.
    component : list
        A list to store vertices of the current connected component.
    """
    visited[v] = True
    component.append(v)
    for neighbor in range(num_vertises):
        if neighbor in graph[v] and not visited[neighbor]:
            dfs(neighbor, component)





def find_conn_comp(graph):
    """
    ...
    """
    num_vertises = len(graph)

    visited = [0] * num_vertises
    all_components = []

    def dfs(v, component):
        """
        Performs a depth-first search (DFS) starting from vertex v, 
        adding all visited vertices to the connected component.
        """
        visited[v] = True
        component.append(v)
        for neighbor in range(num_vertises):
            if neighbor in graph[v] and not visited[neighbor]:
                dfs(neighbor, component)

    for v in range(num_vertises):
        if not visited[v]:
            component = []
            dfs(v, component)
            all_components.append(component)

    return all_components


graph = {0: [1, 2, 8], 1:[0, 2], 2:[0, 1, 8], 3:[], 4:[5], 5:[4, 6], 6:[5, 7], 7:[6], 8:[0, 2]}

print(find_conn_comp(graph))