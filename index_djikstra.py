from queue import PriorityQueue
class Graph:
    def __init__(self, nv):
        self.v = nv
        self.edges = [[-1 for i in range(nv)] for j in range(nv)]
        self.visited = []
def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
def dijkstra(graph, start_vertex):
  D = {v:float('inf') for v in range(graph.v)}
  D[start_vertex] = 0

  pq = PriorityQueue()
  pq.put((0, start_vertex))

  while not pq.empty():
        (dist, curr) = pq.get()
        graph.visited.append(curr)

        for nei in range(graph.v):
            if graph.edges[curr][nei] != -1:
                distance = graph.edges[curr][nei]
                if nei not in graph.visited:
                    old_cost = D[nei]
                    new_cost = D[curr] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, nei))
                        D[nei] = new_cost
  return D

g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 4, 2)
g.add_edge(1, 4, 3)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(4, 3, 5)
g.add_edge(4, 2, 1)
g.add_edge(3, 2, -5)

D = dijkstra(g, 0)

print(D)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
