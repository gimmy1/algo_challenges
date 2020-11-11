# Iterative
def invert_binary_tree_iterative(tree):
    queue = [tree]
    while queue:
        current_node = queue.pop(0)
        if not current_node:
            continue
        swap_nodes(current_node)
        queue.append(current_node.left)
        queue.append(current_node.right)
    return

def invert_binary_tree_recursive(tree):
    if not tree:
        return
    
    swap_nodes(tree.left)
    invert_binary_tree_recursive(tree.left)
    invert_binary_tree_recursive(tree.right)


def swap_nodes(current_node):
    current_node.left, current_node.right = current_node.right, current_node.left
