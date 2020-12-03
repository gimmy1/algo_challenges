class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = "*"
        self.populate_suffix_trie(string)
    
    def populate_suffix_trie(self, string):
        for idx in range(len(string)):
            _string = string[idx:]
            self.insert_substring_starting_at(_string)

    def insert_substring_starting_at(self, _string):
        node = self.root
        for letter in _string:
            if letter not in node:
                node[letter] = {}
            
            node = node[letter]
        
        node[self.end_symbol] = True

    def contains(self, suffix):
        node = self.root
        for letter in suffix:
            if letter not in node:
                return False
            node = node[letter]
        return self.end_symbol in node
    

if __name__ == "__main__":
    sfx = SuffixTrie("babc")
    print(sfx.root)