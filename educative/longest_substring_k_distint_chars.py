def longest_substring_with_k_distinct_characters(string, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(string)):
        if string[window_end] not in char_frequency:
            char_frequency[string[window_end]] = 0
        char_frequency[string[window_end]] += 1

    

        while len(char_frequency) > k:
            char_frequency[string[window_start]] -= 1
            if char_frequency[string[window_start]] == 0:
                del char_frequency[string[window_start]]
            window_start += 1

        max_length = max(max_length, window_end-window_start+1)
    return max_length
        