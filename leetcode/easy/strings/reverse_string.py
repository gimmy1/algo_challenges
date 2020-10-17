def reverse_string(List):
    Half = len(List) // 2
    for idx in range(Half):
        List[idx], List[len(List) - idx - 1] = List[len(List) - idx - 1], List[idx]

    return List

if __name__ == "__main__":
    print(reverse_string(["h","e","l","l","o"]))


