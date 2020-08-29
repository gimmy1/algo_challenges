def word_search(matrix, target_word):
    """
    2-D array of characters, and a target string. Return whether or not the word 
    target word exists in the matrix. Unlike a standard word search, the word must be either
    going left-to-right or top-to-bottom in the matrix.
    [['F', 'A', 'C', 'I'],
     ['O', 'B', 'Q', 'P'],
     ['A', 'N', 'O', 'B'],
     ['M', 'A', 'S', 'S']]
    """
    target_word_list = [let for let in target_word]
    word_length = len(target_word)
    matrix_len = len(matrix)
    i = 0
    while i in range(len(matrix)):
        ji = 0
        while ji in range(len(matrix[i])):
            # LEFT TO RIGHT - FIND OUT IF THERE IS ENOUGH ROOM
            if (len(matrix[i]) - ji) >= word_length:
                count = 0
                x = ji
                while matrix[i][x] == target_word_list[x]:
                    count += 1
                    if count == word_length:
                        return True
                    x += 1
            
            # TOP TO BOTTOM
            if (matrix_len - i) >= word_length:
                count = 0
                y = i
                while matrix[y][ji] == target_word_list[y]:
                    count += 1
                    if count == word_length:
                        return True
                    y += 1
            ji += 1
        i += 1
    return False

if __name__ == "__main__":
    Erin = [
          ['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S'],
        ]
    print(word_search(Erin, "FOAM"))

# 1-d  ['F', 'A', 'M']
# 2-d   #   [
        #   ['F', 'A', 'C', 'I'],
        #   ['O', 'B', 'Q', 'P'],
        #   ['A', 'N', 'O', 'B'],
        #   ['M', 'A', 'S', 'S'],
        # ]