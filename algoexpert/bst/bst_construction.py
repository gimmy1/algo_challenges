class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
class BST:
    def __init__(self):
        self.root = None
    
    def get_node(self, value):
        return self._get_node(value, self.root)
    
    def _get_node(self, value, current_node):
        if current_node is None:
            return False
        
        if value < current_node.value:
            return self._get_node(value, current_node.left)
        elif value > current_node.value:
            return self._get_node(value, current_node.right)
        else:
            return True
    
    def insert_node(self, value):
        self.root = self._insert_node(value, self.root)
    
    def _insert_node(self, value, current_node):
        if current_node is None:
            return Node(value)
        elif value < current_node.value:
            current_node.left = self._insert_node(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._insert_node(value, current_node.right)   
        
        return current_node
    
    def delete_node(self, value):
        self.root = self._delete_node(value, self.root)
    
    def _delete_node(self, value, current_node):
        if current_node is None:
            return None
        
        if value < current_node.value:
            current_node.left = self._delete_node(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete_node(value, current_node.right)
        else:
            # No children
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left and current_node.right:
                smallest_value = self._get_smallest_value(current_node.right)
                
                # delete the smallest value
                current_node.right = self._delete_node(smallest_value.value, current_node.right)
                smallest_value.left = current_node.left
                smallest_value.right = current_node.right
                return smallest_value
            else:
                # only one child
                if current_node.left:
                    return current_node.left
                else:
                    current_node.right
        return current_node

    
    def _get_smallest_value(self, current_node):
        if current_node.left:
            current_node.left = self._get_smallest_value(current_node.left)
        return current_node


if __name__ == "__main__":
    def makeTree():
        bst = BST()
        # import pdb; pdb.set_trace()
        bst.insert_node(5)
        bst.insert_node(3)
        bst.insert_node(4)
        bst.insert_node(7)
        bst.insert_node(2)
        bst.insert_node(6)
        bst.insert_node(8)
        return bst
    bst = makeTree()
    print(bst)
