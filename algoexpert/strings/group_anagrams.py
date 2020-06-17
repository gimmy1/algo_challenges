from collections import defaultdict

def groupanagrams(arr):
    anagrams = defaultdict(list)

    for a in arr:
        sorted_a = "".join(sorted(a))
        anagrams[sorted_a].append(a)
    
    return list(anagrams.values())
    
if __name__ == "__main__":
    print(groupanagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"]))