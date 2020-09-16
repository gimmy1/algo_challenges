from collections import defaultdict
from queue import Queue
love_connections = [("Lysander", "Helena"), ("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                    ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                    ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania")]


# What is breadth-first?
# In contrast to DFS --> we explore all neighbors before moving on
def BFS(adj_list, source, target):
    Q = Queue()
    Q.put(source)
    seen = set()
    while not Q.empty():
        current = Q.get()
        if current == target:
            return True
        for neighbor in adj_list[neighbor]:
            if neighbor not in seen:
                seen.add(neighbor)
                Q.put(neighbor)
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

