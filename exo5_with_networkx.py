import sys

import networkx as nx
from networkx.algorithms import isomorphism


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\n"))

    ancient_graph = nx.Graph()
    ancient_graph.add_edge("A", "F")
    ancient_graph.add_edge("A", "J")
    ancient_graph.add_edge("A", "M")
    ancient_graph.add_edge("B", "C")
    ancient_graph.add_edge("B", "K")
    ancient_graph.add_edge("B", "H")
    ancient_graph.add_edge("C", "D")
    ancient_graph.add_edge("C", "G")
    ancient_graph.add_edge("D", "G")
    ancient_graph.add_edge("D", "L")
    ancient_graph.add_edge("E", "M")
    ancient_graph.add_edge("E", "N")
    ancient_graph.add_edge("E", "G")
    ancient_graph.add_edge("F", "K")
    ancient_graph.add_edge("F", "I")
    ancient_graph.add_edge("H", "I")
    ancient_graph.add_edge("H", "J")
    ancient_graph.add_edge("I", "L")
    ancient_graph.add_edge("J", "N")
    ancient_graph.add_edge("K", "L")
    ancient_graph.add_edge("M", "N")

    modern_graph = nx.Graph()
    for line in lines[1:]:
        frm, to = line.split()
        modern_graph.add_edge(frm, to)
    matcher = isomorphism.GraphMatcher(ancient_graph, modern_graph)
    matcher.is_isomorphic()
    print(matcher.mapping[lines[0]])


if __name__ == "__main__":
    main()
