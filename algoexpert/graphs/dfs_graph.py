class Node:
    def __init__(self, name):
        # WHAT DOES A GRAPH NEED?
        self.name = name
        self.children = []
    
    def add_child(self, name):
        self.children.append(Node(name))
        return self
    
    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(child)
        return array