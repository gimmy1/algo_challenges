def rooms_and_keys(List):
    visited = [False] * len(List)
    _DFS(0, visited, List)
    return all(visited)

def _DFS(idx, visited, List):
    visited[idx] = True
    current = List[idx]
    for key in current:
        if not visited[key]:
            _DFS(key, visited, List)
    
if __name__ == "__main__":
    print(rooms_and_keys([[1], [2], [3], []]))


