from collections import defaultdict
def longestSubstringWithoutDuplication(string):
    largest = ""
    i = 0
    while i < len(string):
        current_string = ""
        seen = defaultdict(int)
        if string[i] not in seen:
            while i < len(string) and string[i] not in seen:
                seen[string[i]] = i 
                current_string += string[i]
                i += 1
            
            if len(current_string) > len(largest):
                largest = current_string
            if i < len(string):
                i = seen[string[i]]
            else:
                return largest
        i += 1
    return largest

if __name__ == "__main__":
    print(longestSubstringWithoutDuplication("clementisacap"))