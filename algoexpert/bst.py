class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left: # first check if there is a left
                return self.left.insert(value)
            else:
                self.left = Node(value)
                return
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
                return
	
    def search(self, value): 
	    if value < self.value:
	    	if self.left:
		    	return self.left.search(value)
		    else:
			    return False
		else:
			if self.right:
				return self.right.search(value)
			else:
				return True
	
	def delete(self, value):
		if value < self.value:
			if self.left:
				self.left = self.left.delete(value)
			else:
				return None
		elif value > self.value:
			if self.right:
				self.right = self.right.delete(value)
			else:
				return None
		else: # found the bum to be deleted
			if self.left is None and self.right is None: # no children
				return None
			elif self.left is None: # deleting a Node with a right child
				tmp = self.right
				self = None
				return tmp
			elif self.right is None:
				tmp = self.left
				self = None
				return tmp
			else:
				current = self.right
				while current.left:
					current = current.left
				self.value = current.value
				self.right = self.right.delete(current.value)
		return self
		

class BST:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = Node(value)
            return True
	
    def search(self, value):
	    if self.root:
			return self.root.search(value)
		else:
			return False
	
	def delete(self, value):
		if self.root is not None:
			self.root = self.root.delete(value)
	
				
    def get_min_value(self):
        pass
		
if __name__ == "__main__":
    bst = BST(6)
	bst.insert(3)
	bst.insert(2)
	bst.insert(4)
	bst.insert(-1)
	bst.insert(1)
	bst.insert(-2)
	bst.insert(8)
	bst.insert(7)

	print("before deletion:")
	display(bst.root)

	bst.delete(10)
	print("after deletion:")
	display(bst.root)