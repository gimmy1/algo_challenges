def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    i = 0
    unique = [iterable[0]]
    while i < len(iterable) - 1:
        if iterable[i] != unique[-1]:
            unique.append(iterable[i])
        i += 1
    return unique


if __name__ == "__main__":
    print(unique_in_order("AAABBBCCCcADDD"))
