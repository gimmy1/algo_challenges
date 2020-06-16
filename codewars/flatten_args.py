def flatten(*argv):
    i = 0
    flattened = []
    while i < len(argv):
        if isinstance(argv[i], list):
            flattened.extend(flatten(*argv[i]))
        else:
            flattened.append(argv[i])
        i += 1
    return flattened

if __name__ == "__main__":
    print(flatten(1, [2, [3]], 4, 5, [6, [7]]))