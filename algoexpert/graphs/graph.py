class Graph:
    """
    # Initialize empty Graph with V vertices and 0 edges
    """
    def __init__(self, V):
        self._V = V
        self._E = 0
        # initialize an adjacency list for each vertex
        self.adjacency_list = [[] for i in range (0, V)]
    
    # returns the number of vertices in the Graph
    def V(self):
        return self.V
    
    # returns the number of edges in the graph
    def E(self):
        return self.E
    
    # add edge between u-v in this graph, u,v are vertices
    def add_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        self._E += 1
        self.adjacency_list[v].append(u)
        self.adjacency_list[u].append(v)

    # returns all the neighbors of vertex v
    def adjacency(self, v):
        self._validate_vertex(v)
        return self.adjacency_list[v]
    
    # helper function to validate vertices
    def _validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise Exception(f"Vertex {v} is not between 0 and {self.V - 1}")


if __name__ == "__main__":
    # Convert integers stored in the graph back to the real-world names
    vertices = ["Albert", "Bob", "Christa", "Danielle"]
    V = len(vertices)
    G = Graph(V)

    # Add the relationships
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,3)
    G.add_edge(2,3)

    print(type(G.adjacency_list))