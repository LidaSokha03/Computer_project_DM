"""
CLI for the whole project
"""
import argparse
from library.articulation import find_points
from library.articulation import bridges
from library.components import find_conn_comp
from library.graph_visual import graph_visualization
from library.read_write import read_graph
from library.read_write import write_graph
from library.strong_con import kosaraju_scc


def main():
    """
    ...
    """
    parser = argparse.ArgumentParser(
        prog='Graph connectivity analysis',
        description='The program reads a graph from a file, searches for connectivity components\
(also of strong connectivity), finding connection points and bridges on the graph')


    parser.add_argument('file', type = str, help='Graph file')
    parser.add_argument(
        "--is_oriented",
        action = 'store_true',
        help="Oriented/Disoriented")
    parser.add_argument(
        "--file_path_save",
        type=str,
        default='graph',
        help="Path to new file")
    parser.add_argument(
        "--save_to_file",
        action = 'store_true',
        help="Saving graph to file")
    parser.add_argument(
        "--connectivity",
        action = 'store_true',
        help="Finding connection points")
    parser.add_argument("--bridges", action = 'store_true', help="Finding bridges")
    parser.add_argument("--components", action = 'store_true', help="Connectivity components")
    parser.add_argument(
        "--strong_components",
        action = 'store_true',
        help="Strong connectivity components")
    parser.add_argument("--visualisation", action = 'store_true', help="Graph visualization")

    args = parser.parse_args()

    oriented = args.is_oriented
    graph = read_graph(args.file, oriented)

    if args.connectivity:
        try:
            result = find_points(graph, oriented)
            print(f'Connecting points: {result}')
        except ValueError:
            print("The graph is oriented. Searching for connecting points is not possible.")

    elif args.bridges:
        try:
            result = bridges(graph, oriented)
            print(f'Bridges: {result}')
        except ValueError:
            print("The graph is oriented. Searching for bridges is not possible.")

    elif args.components:
        try:
            result = find_conn_comp(graph, oriented)
            print(f'Connectivity components: {result}')
        except ValueError:
            print("The graph is oriented. Searching for connected components is not possible.")

    elif args.strong_components:
        result = kosaraju_scc(graph, oriented)
        if result == -1:
            print("The graph is not oriented. Searching for strong connected components is not possible.")
        else:
            print(f'Strong connectivity components: {result}')

    elif args.visualisation:
        graph_visualization(graph, oriented)

    elif args.save_to_file:
        file_to_save = args.file_path_save
        if '.' not in file_to_save:
            file_to_save += '.csv'
        write_graph(graph, file_to_save)
        print(f"Graph saved to {file_to_save}")

    else:
        print("Error. You should choose any function.")
        parser.print_help()


if __name__ == "__main__":
    main()