def find_points(graph):
    """
    ...
    """
    ...


def bridges(graph):
    """
    Find all bridges in an undirected graph.
    """
    bridges_list = []
    copied_graph = graph.copy()
    for edge in copied_graph:
        graph.pop(edge)
        values = []
        for key in graph:
            for value in graph.get(key):
                values.append(value)
            values.append(key)

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
