"""
Set of functions for working with file
Reading graph from file
Writing graph in new file
"""
def read_graph(filename, is_oriented: bool):
    """
    Function that reads graph from file
    :param filename: str, the name or path to the file
    :return: dict, where key - node and items below the key are nodes connented with key node
    """
    nodes = set()
    graph = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line  = line.rstrip().split(',')
            for node in line:
                if node not in nodes:
                    nodes.add(node)
                    graph[node] = []
            if len(graph.keys()) == len(nodes):
                if is_oriented:
                    for i, el in enumerate(line):
                        if i == 0:
                            graph[el].append(line[1])
                else:
                    for i, el in enumerate(line):
                        if i == 0:
                            graph[el].append(line[1])
                        elif i == 1:
                            graph[el].append(line[0])

    return graph


def write_graph(graph, new_filename):
    """
    Function that wrines graph in new file
    :param graph: dict, where key - node and items below the key are nodes connented with key node
    :param new_filename: str, new file name
    :return: None
    """
    with open(new_filename, 'w', encoding='utf-8') as file:
        for main_node, else_nodes in graph.items():
            for node in else_nodes:
                file.write(f'{str(main_node)},')
                file.write(str(node))
                file.write('\n')
