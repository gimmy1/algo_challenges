def permutations_recursive(arr):
    perms = []
    permutations_helper(0, arr, perms)
    return perms

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def permutations_helper(idx, arr, perms):
    if idx == len(arr) - 1:
        perms.append(arr[:])
    else:
        for j in range(idx, len(arr)):
            swap(arr, idx, j)
            permutations_helper(idx+1, arr, perms)
            swap(arr, idx, j)


if __name__ == "__main__":
    print(permutations_recursive([1,2,3]))