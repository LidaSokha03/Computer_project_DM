"""
CLI for the whole project
"""
import argparse
from articulation import find_points
from articulation import bridges
from components import find_conn_comp
from graph_visual import graph_visualization
from read_write import read_graph
from strong_con import kosaraju_scc


def main():
    """
    ...
    """
    parser = argparse.ArgumentParser(
        prog='Аналіз звʼязності графів',
        description='Програма виконує читання графу з файлу, шукає компоненти звʼязності\
(також сильної звʼязності), пошук точок сполучення та мостів на графі')

    parser.add_argument('file', type = str, help='Файл графу')
    parser.add_argument(
        "--is_oriented",
        action = 'store_true',
        help="Орієнтованість/неорієнтованість графу")
    parser.add_argument(
        "--connectivity",
        action = 'store_true',
        help="Знаходження точок сполучення")
    parser.add_argument("--bridges", action = 'store_true', help="Знаходження мостів")
    parser.add_argument("--components", action = 'store_true', help="Компоненти звʼязності")
    parser.add_argument(
        "--strong_components",
        action = 'store_true',
        help="Компоненти сильної звʼязності")
    parser.add_argument("--visualisation", action = 'store_true', help="Візуалізація графу")

    args = parser.parse_args()

    oriented = args.is_oriented
    graph = read_graph(args.file, oriented)

    if args.connectivity:
        result = find_points(graph, oriented)
        print(f'Точки сполучення в графі: {result}')
    elif args.bridges:
        result = bridges(graph, oriented)
        print(f'Мости у графі: {result}')
    elif args.components:
        result = find_conn_comp(graph, oriented)
        print(f'Компоненти звʼязності: {result}')
    elif args.strong_components:
        result = kosaraju_scc(graph, oriented)
        print(f'Компоненти сильної звʼязності: {result}')
    elif args.visualisation:
        graph_visualization(graph, oriented)
    else:
        print("Помилка: необхідно вибрати одну з функцій.")
        parser.print_help()


if __name__ == "__main__":
    main()
