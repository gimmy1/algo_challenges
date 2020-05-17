def flatten(arr):
    flat = []
    for a in arr:
        if isinstance(a, list):
            flat.extend(flatten(a))
        else:
            flat.append(a)
    return flat

if __name__ == "__main__":
    print(flatten([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))