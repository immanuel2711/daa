class Graph:
    def __init__(self, vert):
        self.V = vert
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, par, i):
        if par[i] == i:
            return i
        return self.find(par, par[i])

    def apply_union(self, par, rank, x, y):
        xroot = self.find(par, x)
        yroot = self.find(par, y)
        if rank[xroot] < rank[yroot]:
            par[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            par[yroot] = xroot
        else:
            par[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        rslt = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        par = []
        rank = []
        for node in range(self.V):
            par.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(par, u)
            y = self.find(par, v)
            if x != y:
                e = e + 1
                rslt.append([u, v, w])
                self.apply_union(par, rank, x, y)
        for u, v, weight in rslt:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 4, 2)
g.add_edge(1, 4, 3)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(4, 3, 5)
g.add_edge(4, 2, 1)
g.add_edge(3, 2, -5)
g.kruskal_algo()
