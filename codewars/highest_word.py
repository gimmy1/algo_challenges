import string
def highest_word(s):
    alphabet_list = list(string.ascii_letters)
    values = [i for i in range(1, len(alphabet_list))]
    alphabet_values = dict(zip(alphabet_list, values))
    
    i = 0
    longest_count = float("-inf")
    index = 0
    word = ""
    while i < len(s) - 1:
        current_count = 0
        while i < len(s) and s[i] != " ":
            current_count += alphabet_values[s[i]]
            i += 1
        
        # import pdb; pdb.set_trace()
        if current_count > longest_count:
            longest_count = current_count
            word = s[index: i]
    
        i += 1
        index = i
    return word

        


if __name__ == "__main__":
    print(highest_word('man i need a taxi up to ubud'))