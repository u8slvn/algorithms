from collections import namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, value')
Edge.__new__.__defaults__ = (1,)


class Graph:
    def __init__(self, edges):
        wrong_edges = [edge for edge in edges if len(edge) not in [2, 3]]
        if wrong_edges:
            raise ValueError(f"Wrong formatted edges: {wrong_edges}.")
        self.edges = [Edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(([edge.start, edge.end] for edge in self.edges), [])
        )

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.value))
        return neighbours

    def dijkstra(self, source, dest):
        distances = {vertex: inf for vertex in self.vertices}
        distances[source] = 0
        previous_vertices = {vertex: None for vertex in self.vertices}
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices,
                key=lambda vertex: distances[vertex]
            )
            vertices.remove(current_vertex)

            if distances[current_vertex] == inf:
                break

            for neighbour, value in self.neighbours[current_vertex]:
                new_value = distances[current_vertex] + value
                if new_value < distances[neighbour]:
                    distances[neighbour] = new_value
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = [], dest
        while previous_vertices[current_vertex] is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.insert(0, current_vertex)
        return path


edges = [
    ('A', 'B', 5), ('A', 'C', 3), ('A', 'D', 2), ('B', 'F', 2), ('D', 'C', 1),
    ('C', 'E', 4), ('C', 'F', 7), ('E', 'G', 9), ('F', 'G', 10),
]

graph = Graph(edges=edges)
print(graph.dijkstra(source='A', dest='G'))
