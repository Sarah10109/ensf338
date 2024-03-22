class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # The main function to construct MST using Kruskal's algorithm
    def mst(self):
        result = []  
        i, e = 0, 0  # An index and edge.

        self.graph = sorted(self.graph, key=lambda item: item[2])

        nodes = [i for i in range(self.V)]

        def find(i):
            if nodes[i] == i:
                return i
            return find(nodes[i])

        
        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot != yroot:
                nodes[yroot] = xroot

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = find(u)
            y = find(v)

            # If including this edge does not cause cycle, include it in result and increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                union(x, y)

        # create a new Graph object for the MST
        mst_graph = Graph(self.V)
        for u, v, w in result:
            mst_graph.add_edge(u, v, w)

        return mst_graph