'''
Graph represented in code
'''




from turtle import distance


num_nodes = 5
edges = [(0,1) , (0,4) , (1,4) , (1,3) , (1,2) , (2,3) , (3,4)]

# This is not most efficient way to represent a graph. Its okay to help you Visualize and draw graph.

class Graph:
    def __init__(self , num_nodes , edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]

        for n1 , n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    
    def __repr__(self):
        return "\n".join(["{} : {}".format(n , neighbros)for n , neighbros in enumerate(self.data)])
    
    def __str__(self):
        return self.__repr__()

    def add_edge(self , a , b):
        self.data[a].append(b)
        self.data[b].append(a)

    def del_edge(self , a , b):
        for i in range(len(self.data[a])):
            if (self.data[a][i] == b):
                self.data[a].pop(i)
                break

        for i in range(len(self.data[b])):
            if (self.data[b][i] == a):
                self.data[b].pop(i)
                break

    
            
graph1 = Graph(num_nodes , edges)
#graph1.add_edge(0 , 3)
#graph1.del_edge(1 , 4)
#print(graph1)



num_nodes2 = 9
edges2 = [( 0,1) , (0,3) , (1,2) , (2,3) , (4,5) , (4,6) , (5,6) , (7,8)]
graph2 = Graph(num_nodes2 , edges2) 

'''
Question: Implement breadth-first search given a source node in a graph using Python.

 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as discovered
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as discovered then
11                  label w as discovered
12                  Q.enqueue(w)
​
'''

def bfs(graph , root):
    queue = []

    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)

    discovered[root] = True
    queue.append(root)

    distance[root] = 0
    idx = 0

    while idx < len(queue):
        current = queue[idx]
        idx += 1

        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    all_connected = True if len(queue) == len(graph.data) else False
    return queue , distance , parent , all_connected

#print(bfs(graph1 , 3))
#print(bfs(graph2 , 5))

def dfs(graph , root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)

            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)
    return result

#print(dfs(graph1 , 3))


'''
Write a class to represent Weighted and Directional graphs
'''

class wdGraph:
    def __init__(self , num_nodes , edges , weighted = False  , directed = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
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

    def __repr__(self):
        result = ""
        if self.weighted:
            for i , (nodes , weights) in enumerate(zip(self.data , self.weights)):
                result += "{}:{} \n".format(i , list(zip(nodes , weights)))
        else:
            for i , nodes in enumerate(self.data):
                result += "{}:{}\n".format(i , nodes)
        return result

    def __str__(self):
        return self.__repr__()


num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

exampleWG = wdGraph(num_nodes5 , edges5 , weighted=True)
print(exampleWG)
print('#####################################################')
num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
exampleDG = wdGraph(num_nodes6 , edges6 , directed=True)
print(exampleDG)


'''
Question: Write a function to find the length of the shortest path between two nodes in a weighted directed graph.
'''



def shortest_path(graph , source , target):
    visited = [False] * len(graph.data)
    distance = [float("inf")] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        idx += 1
        visited[current] = True

        # update distance beetwen nodes

        update_distances(graph , current , distance)

        next_node = pick_next_node(distance , visited)

        if next_node:
            queue.append(next_node)
        
    return distance[target]


def update_distances(graph , current , distance , parent = None):
    # Update the distance of the current nodes neighbros
    neighbros = graph.data[current]
    weights = graph.weights[current]

    for i , node in enumerate(neighbros):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = parent


def pick_next_node(distance , visited):
    # pick next unvisited node with the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_distance = distance[node]
            min_node = node
    return min_node

