class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
    
    def insert(self, v):
        if v < self.v:
            if self.left: 
                return self.left.insert(v)
            else:
                self.left = Node(v)
                return
        else:
            if self.right:
                return self.right.insert(v)
                
            else:
                self.right = Node(v)
                return
    
    def search(self, v):
        if v < self.v:
            if self.left:
                return self.left.search(v)
        elif v > self.v:
            if self.right:
                return self.right.search(v)
        return False
        
    def remove(self, v):
        if v < self.v:
            if self.left:
                return self.left.remove(v)
            else:
                return None
        elif v > self.v:
            if self.right:
                return self.right.remove(v)
            else:
                return None
        
        # CASES
        if not self.left and not self.right:
            return_val = self.v
            self.v = None
            return return_val
        elif not self.left:
            swap_val = self.right.v
            return_val = self.v
            self.v = swap_val
            return return_val
        elif self.left and self.right:
            current = self.right
            while current.left:
                current = current.left
            
            return_val = self.v
            self.v = current.v
            return

    def find_closest(self, v):
        pass
        


class BinarySearchTree:
    def __init__(self, v):
        self.root = None
    
    def insert(self, v):
        if self.root:
            self.root.insert(v)
            return
        else:
            self.root = Node(v)
    
    def search(self, v):
        if self.root:
            return self.root.search(v)

        else:
            return False
    
    def remove(self, v):
        if self.root:
            return self.root.remove(v)
        return None
        
    def find_closest(self, v):
        if self.root:
            return self.root.find_closest(v)
        return None