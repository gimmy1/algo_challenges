def selection_sort(List):
    idx = 0
    while idx < len(List):
        smallest_val = List[idx]
        smallest_idx = idx
        for jdx in range(idx+1, len(List)):
            if List[jdx] < smallest_val:
                smallest_val = List[jdx]
                smallest_idx = jdx
        # import pdb; pdb.set_trace()
        List[idx], List[smallest_idx] = List[smallest_idx], List[idx]
        idx += 1
    return List

if __name__ == "__main__":
    print(selection_sort([8,5,2,9,5,6,3]))

