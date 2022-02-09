from re import L
from turtle import distance


class Graph:
    def __init__(self , num_nodes , edges , weighted = False , directed = True):
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.directed = directed

        self.data = [[] for _ in range(num_nodes)]
        self.weights = [[] for _ in range(num_nodes)]

        for edge in edges:
            if self.weighted:
                node1 , node2 , weight = edge
                self.data[node1].append(node2)
                self.weights[node1].append(weight)

                if not directed:
                    self.data[node2].append(node1)
                    self.weights[node2].append(weight)
            else:
                node1 , node2 = edge
                self.data[node1].append(node2)

                if not directed:
                    self.data[node2].append(node1)


def shortest_path(graph , source , target):
    visited = [False] * len(graph.data)
    distances = [float("inf")] * len(graph.data)
    distances[source] = 0

    queue = []
    queue.append(source)
    idx = 0

    while not visited[target] and len(queue) > idx:
        current = queue[idx]
        visited[current] = True
        idx += 1

        calculate_new_distances(graph , current , distances)
        next_node = pick_next_node(distances , visited)

        if next_node:
            queue.append(next_node)
    return distances[target]


def calculate_new_distances(graph , current  , distances , parent = None):
    neighbros = graph.data[current]
    weights = graph.weights[current]

    for i , node in enumerate(neighbros):
        weight = weights[i]
        if distances[current] + weight < distances[node]:
            distances[node] = distances[current] + weight
            if parent:
                parent[node] = parent

def pick_next_node(distances , visited):
    min_distance = float("inf")
    min_node = None
    for node in range(len(distances)):
        if not visited[node] and distances[node] < min_distance:
            min_node = node
            min_distance = distances[node]
    return min_node

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]

graph1 = Graph(num_nodes7 , edges7 , directed=True , weighted=True)
print(shortest_path(graph1 , 0 , 5))