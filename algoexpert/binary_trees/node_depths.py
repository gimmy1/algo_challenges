def node_depths_iterative(root):
    sum_of_depths = 0
    nodes = [{"node": root, "depth": 0}]
    while nodes: # truthy value
        nodes_info = nodes.pop()
        node, depth = nodes_info["node"], nodes_info["depth"]
        if not node:
            continue
        sum_of_depths += depth
        nodes.append({"node": node.left, "depth": depth + 1}) # left
        nodes.append({"node": node.right, "depth": depth + 1}) # left
    return sum_of_depths

def node_depth_recursive(root, depth=0):
    if not root:
        return 0
    
    return depth + node_depth_recursive(root.left, depth + 1) + node_depth_recursive(root.right, depth + 1)



class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None