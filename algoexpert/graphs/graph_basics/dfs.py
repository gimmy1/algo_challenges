from collections import defaultdict
love_connections = [("Lysander", "Helena"), ("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                    ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                    ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania")]


# What is breadth-first?
# In contrast to DFS --> we explore all neighbors before moving on
def DFS(adj_list, source, target):
    visited = set()
    return _DFS(adj_list, source, target, visited)

def _DFS(adj_list, curr, target, visited):
    if curr == target:
        return True
    
    if curr in visited:
        return False
    
    visited.add(curr)
    for neighbor in adj_list[curr]:
        if _DFS(adj_list, neighbor, target, visited):
            return True
    
    return False



def adjacency_list_transform(graph_ds):
    adj_list = defaultdict(list)
    for source, target in graph_ds:
        adj_list[source].append(target)
    return adj_list

if __name__ == "__main__":
    adj_list = adjacency_list_transform(love_connections)
    print(BFS(adj_list, "Hermia", "Oberon"))
    # print(adj_list)

