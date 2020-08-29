from collections import defaultdict
def find_concatenated_words(List):
    all_words = defaultdict(bool)
    for idx, li in enumerate(List):
        if li not in all_words:
            all_words[li] = False
        else:
            all_words[li] = True
        create_concatenated_words(li, List[:idx], all_words)
        # import pdb; pdb.set_trace()
    return [k for k, v in all_words.items() if v == True]
        
def create_concatenated_words(word, List, _dict):
    for key in List:
        in_front = f"{word}{key}"
        behind = f"{key}{word}"
        if in_front != behind:
            add_word_to_dictionary(_dict, in_front, behind)
        else:
            add_word_to_dictionary(_dict, in_front)


def add_word_to_dictionary(_dict, *argv):
    for a in argv:
        if a not in _dict:
            _dict[a] = False
        else:
            _dict[a] = True
        # import pdb; pdb.set_trace()

if __name__ == "__main__":
    words = ["catsdog", "rat", "cats", "cat", "dog", "dogcat"]
    
    print(find_concatenated_words(words))