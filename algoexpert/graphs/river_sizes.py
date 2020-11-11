def riverSizes(matrix):
    # Write your code here.
    sizes = []
	visited = [[False for value in row] for row in matrix]
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if not visited[row][col]:
				traverse_node(row, col, matrix, visited, sizes)
	return sizes

def traverse_node(row, col, matrix, visited, sizes):
	river_size = 0
	queue = [[row, col]]
	# depth-first-search
	while queue:
		current_node = queue.pop()
		row = current_node[0]
		col = current_node[1]
		if visited[row][col]:
			continue
		visited[row][col] = True
		if matrix[row][col] == 0:
			continue
		visited[row][col] = True
		river_size += 1
		unvisited_neighbors = get_unvisited_neigbors(row, col, matrix, visited)
		for neighbor in unvisited_neighbors:
			queue.append(neighbor)
	if river_size > 0:
		sizes.append(river_size)

def get_unvisited_neigbors(row, col, matrix, visited):
	unvisited_neighbors = []
	if row > 0 and not visited[row-1][col]:
		unvisited_neighbors.append([row-1, col])
	if row < len(matrix) - 1 and not visited[row+1][col]:
		unvisited_neighbors.append([row+1, col])
	if col > 0 and not visited[row][col-1]:
		unvisited_neighbors.append([row, col-1])
	if col < len(matrix[0]) - 1 and not visited[row][col+1]:
		unvisited_neighbors.append([row, col+1])
	return unvisited_neighbors

if __name__ == "__main__":
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]]
    river_sizes(matrix)