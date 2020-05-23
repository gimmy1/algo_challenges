class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
    
    def insert_node(self, v):
        if v < self.v:
            if self.left:
                self.left.insert_node(v)
            else:
                self.left = Node(v)
                return
        else:
            if self.right:
                self.right.insert_node(v)
            else:
                self.right = Node(v)
                return
    
    def branch_sums(self):
        import pdb; pdb.set_trace()
        if self.left is None and self.right is None:
            pass
        return (self.v + self.left.branch_sums() + self.left.branch_sums())


class BinaryTree:
    def __init__(self, v):
        self.root = Node(v)
    
    def insert_node(self, v):
        self.root.insert_node(v)
    
    def branch_sums(self):
        if self.root is None:
            return 0
        return self.root.branch_sums()



def branch_sums(root):
    if root == None:
        return 0
    return root.v + (branch_sums(root.left) + branch_sums(root.right))

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    root = BinaryTree(2)  
    root.insert_node(5)
    root.insert_node(13)
    root.insert_node(15)
    root.insert_node(19)
    root.insert_node(-1)
    root.insert_node(-10)
    root.insert_node(25)

    _sum = root.branch_sums()
    print(_sum)

