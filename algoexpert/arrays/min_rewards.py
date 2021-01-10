def minRewards(scores):
    # Write your code here.
    rewards = [1 for _ in scores]
	
    local_min_idxs = get_local_min_indexes(scores)
    for local_min_idx in local_min_idxs:
        expand_from_local_min_idx(local_min_idx, scores, rewards)
    return sum(rewards)

def get_local_min_indexes(array):
	if len(array) == 1:
		return [0]
	local_min_indexes = []
	for idx in range(len(array)):
		if idx == 0 and array[idx] < array[idx + 1]:
			local_min_indexes.append(idx)
		if idx == len(array) - 1 and array[idx] < array[idx-1]:
			local_min_indexes.append(idx)
		if idx == 0 or idx == len(array) - 1:
			continue
		if array[idx] < array[idx+1] and array[idx] < array[idx-1]:
			local_min_indexes.append(idx)
	return local_min_indexes

def expand_from_local_min_idx(local_min_idx, scores, rewards):
	left_idx = local_min_idx - 1
	while left_idx >= 0 and scores[left_idx] > scores[left_idx + 1]:
		rewards[left_idx] = max(rewards[left_idx], rewards[left_idx + 1] + 1)
		left_idx -= 1
	right_idx = local_min_idx + 1
	while right_idx < len(scores) and scores[right_idx] > scores[right_idx - 1]:
		rewards[right_idx] = rewards[right_idx - 1] + 1
		right_idx += 1

if __name__ == "__main__":
    print(minRewards([8,4,3,1,2,3,4,9,5]))