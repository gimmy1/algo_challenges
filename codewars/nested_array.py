def sum_nested_numbers(arr, m=1):
    total = 0
    for a in arr:
        if isinstance(a, list):
            total += sum_nested_numbers(a, m+1)
        else:
            total += a ** m
        # nested = 0
    return total


if __name__ == "__main__":
    print(sum_nested_numbers([1, [2], 3, [4, [5]], 1]))