def check_anagram(st, ts):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(st) != len(ts): return False
    anagram1 = {}
    anagram2 = {}
    for ab, ba in zip(st, ts):
        print(ab, ba)
        # import pdb; pdb.set_trace()
        try:
            anagram1[ab] += 1
        except KeyError:
            anagram1[ab] = 1
        try:
            anagram2[ba] += 1
        except KeyError:
            anagram2[ba] = 1

    
    return anagram1 == anagram2

if __name__ == "__main__":
    print(check_anagram("anagram", "nagaram"))