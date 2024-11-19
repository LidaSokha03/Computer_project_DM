"""
The visualization of directed and undirected graphs
"""
import networkx as nx
import matplotlib.pyplot as plt


def graph_visualization(graph, is_directed: bool):
    """
    The fuction for Graph visualization. 
    :param graph: dict, each key is a certain node
    and items below the keys are nodes that are connected with key node
    :param is_directed: bool, True if directed graph, False undirected graph.
    :return: None
    """
    if is_directed:
        g = nx.DiGraph()
    else:
        g = nx.Graph()

    for node in graph.keys():
        g.add_node(node)

    for main_node, else_nodes in graph.items():
        for node in else_nodes:
            g.add_edge(main_node, node)


    nx.draw(g, with_labels = True, node_color='yellowgreen', node_size=500,\
edge_color='goldenrod', font_size=10)
    plt.show()


graph_visualization({1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}, False)
graph_visualization({1: [2, 1], 2: [1, 3], 3: [2, 3]}, False)
graph_visualization({1: [2, 3, 4, 5], 2: [1], 3: [1], 4: [1], 5: [1]}, False)
graph_visualization({1: [2], 2: [3, 4], 3: [4], 4: []}, True)
graph_visualization({1: [2], 2: [3], 3: [4], 4: [1]}, False)
graph_visualization({1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}, False)
graph_visualization({1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}, True)
graph_visualization({1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, False)
graph_visualization({1: [2], 2: [1], 3: [], 4: []}, False)
graph_visualization({1: [2, 3], 2: [1], 3: [1, 4, 5], 4: [3], 5: [3]}, True)
graph_visualization({\
1: [2, 3, 4],\
2: [1, 5, 6],\
3: [1, 7, 8],\
4: [1, 9, 10],\
5: [2, 11, 12],\
6: [2, 13, 14],\
7: [3, 15],\
8: [3, 16],\
9: [4, 17],\
10: [4, 18],\
11: [5, 19],\
12: [5, 20],\
13: [6],\
14: [6],\
15: [7],\
16: [8],\
17: [9],\
18: [10],\
19: [11],\
20: [12]\
}, True)
