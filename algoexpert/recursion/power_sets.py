def powersets(arr):
    subsets = [[]]
    for ele in arr:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [ele])
    return subsets

if __name__ == "__main__":
    print(powersets([1, 2, 3]))