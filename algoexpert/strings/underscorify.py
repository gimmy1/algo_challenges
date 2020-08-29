def underscorify_substring(String, search_string):
    underscorified = []
    split_string = String.split(" ")
    for sub_string in split_string:
        # import pdb; pdb.set_trace()
        if len(sub_string) >= 4:
            underscorified.append(find_all_occurrences(sub_string, search_string))
        else:
            underscorified.append(sub_string)
    return " ".join(underscorified)
        

def find_all_occurrences(substring, search_string):
    occurrences = []
    length = len(search_string)
    for i, _ in enumerate(substring):
        if substring[i: i+length].find(search_string) > -1:
            occurrences.append([i, i+length])
    collapsed = collapse_overlapping_occurences(occurrences)
    if collapsed:
        return underscorify_it(collapsed, substring)
    return substring

def collapse_overlapping_occurences(occurences):
    collapsed = []
    for _, v in enumerate(occurences, 1):
        # [(0,4), (4, 8)]
        try:
            if v[0] <= collapsed[-1][1]:
                collapsed[-1][1] = v[1]
        except IndexError:
            collapsed.append(v)
    return collapsed

def underscorify_it(indexes, substring):
    underscored = ""
    for i, v in enumerate(substring):
        # import pdb; pdb.set_trace()
        if i == indexes[0][0]:
            underscored += "_" + v
        elif i == indexes[0][1] - 1:
            underscored += v + "_"
        else:
            underscored += v
    return underscored
    

    
        
if __name__ == "__main__":
    print(underscorify_substring("testthis is a testtest to see if testestest it works", "test"))