from collections import defaultdict, Counter
def ransom_note(ransom_note, magazine):
    if len(magazine) < len(ransom_note): return False
    
    ransom = defaultdict(int)
    mag = defaultdict(int)
    for idx, char in enumerate(magazine):
        try:
            mag[char] += 1
            ransom[ransom_note[idx]] += 1
        except IndexError:
            pass
    
    for key, val in ransom.items():
        if key not in mag:
            return False
        if val > mag[key]:
            return False
    
    return True

def ransom_note_two(r, m):
    if len(m) < len(r): return False
    
    magazine = Counter(m)
    for v in r:
        if v not in magazine or magazine[v] <= 0:
            return False
        
        magazine[v] -= 1
    
    return True

if __name__ == "__main__":
    print(ransom_note_two("aac", "aaaaaaabaa"))


