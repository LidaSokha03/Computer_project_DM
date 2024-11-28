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
