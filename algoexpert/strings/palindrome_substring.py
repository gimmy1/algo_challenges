def longest_palindromic_substring(string):
    curr_longest = [0,1]
    for i in range(1, len(string)):
        odd = get_largest_palindrome(string, i-1, i+1)
        even = get_largest_palindrome(string, i-1, i)
        longest = max(odd, even, key=lambda x: abs(x[0] - x[1]))
        curr_longest = max(curr_longest, longest, key=lambda x: abs(x[0] - x[1]))
    return string[curr_longest[0]: curr_longest[1]]

def get_largest_palindrome(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left+1, right]

if __name__ == "__main__":
    print(longest_palindromic_substring("abaxyzzyxf"))