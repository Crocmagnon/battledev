import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + " adjacent: " + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor):
        self.adjacent[neighbor] = True

    def get_connections(self):
        return self.adjacent.keys()


class Graph:
    def __init__(self):
        self.vert_dict = {}

    def __iter__(self):
        return iter(self.vert_dict.values())

    def __str__(self):
        res = []
        for vertex in self:
            res.append(str(vertex))
        return "\n".join(res)

    def add_vertex(self, node):
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        self.vert_dict.get(n)

    def add_edge(self, frm, to):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to])
        self.vert_dict[to].add_neighbor(self.vert_dict[frm])

    def get_vertices(self):
        return self.vert_dict.keys()


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\n"))

    ancient_graph = Graph()
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
    print(ancient_graph)

    modern_graph = Graph()
    for line in lines[1:]:
        frm, to = line.split()
        modern_graph.add_edge(frm, to)
    print(modern_graph)


if __name__ == "__main__":
    main()
