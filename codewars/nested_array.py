def sum_nested_numbers(arr, depth=1):
    total = 0
    for a in arr:
        if isinstance(a, list):
            total += sum_nested_numbers(a, depth+1)
        else:
            total += a ** depth
    return total


if __name__ == "__main__":
    print(sum_nested_numbers([1, [2], 3, [4, [5]], 1]))