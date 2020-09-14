# CREATE THIS with a Graph Class: takes in a length of vertices
# [[1, 2, 3], [0], [0, 3], [0, 2]]
from random import randrange
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self._V = V # number of vertices
        self._E = 0
        # create initial structure for vertices and edges to be placed in. 
        self.graph_display = [[] for i in range(V)]
        self.adjacency_list = defaultdict(list)

    def V(self):
        return self._V
    
    def E(self):
        return self._E
    
    def _validate_vertex_input(self, v):
        if v < 0 or v >= self._V:
            raise Exception("Dude, no bueno")
        return True
    
    def add_edges_to_initial_graph(self, v, u):
        if self._validate_vertex_input(v):
            # [0,1]->[[1],[0]];
            # [0,2]->[[1,2],[0],[0]];
            # [0,3]->[[1,2,3],[0],[0],[0]];
            # [2,3]->[[1,2,3],[0],[0,3],[0,2]];
            self.graph_display[v].append(u)
            self.graph_display[u].append(v)
            self._E += 1
        
    # def transform_to_adjacency_list(self):
    #     if not self._E:
    #         raise Exception("Empty Graph array")
        
    #     for source in self.graph_display:
    #         self.adjacency_list[source[0]].append()
        

if __name__ == "__main__":
    random_graph_vertex = 4
    g = Graph(random_graph_vertex)

    # for i in range(random_graph_vertex):
    g.add_edges_to_initial_graph(3, 2)
    g.add_edges_to_initial_graph(0, 3)
    g.add_edges_to_initial_graph(0, 2)
    g.add_edges_to_initial_graph(0, 1)
    g.add_edges_to_initial_graph(1, 3)

    # g.transform_to_adjacency_list()

    print(g.adjacency_list)

        


