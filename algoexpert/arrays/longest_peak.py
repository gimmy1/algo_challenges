def longest_peak(List):
    idx = 1
    longest_peak = 0
    while idx < len(List):
        is_peak = List[idx-1] < List[idx] and List[idx] > List[idx+1]
        if not is_peak:
            idx += 1
            continue
        
        left_idx = idx - 2
        while left_idx > 0 and List[left_idx] < List[left_idx+1]:
            left_idx -= 1
        
        right_idx = idx + 2
        while right_idx < len(List) and List[right_idx] < List[right_idx - 1]:
            right_idx += 1

        current_peak = right_idx - left_idx - 1
        longest_peak = max(longest_peak, current_peak)
        i = right_idx
    return longest_peak

if __name__ == "__main__":
    print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))