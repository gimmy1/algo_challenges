def flatten(*argv):
    flatten_arr = []
    i = 0
    while i < len(argv):
        if isinstance(argv[i], list):
            flatten_arr.extend(flatten(argv[i]))
        else:
            flatten_arr.append(argv[i])
        i += 1
    return flatten_arr

if __name__ == "__main__":
    print(flatten(1, [2, 3], 4, 5, [6, [7]]))
