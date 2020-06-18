def count_say_sequence(sequence):
    sequences = ["1", "11"]
    if sequence == 1: return "1"
    if sequence == 2: return "11"
    for i in range(3, sequence+1):
        read_sequence = sequences[i-2]
        k = 0
        new_str = ""
        while k < len(read_sequence):
            count = 0
            prev_val = read_sequence[k]
            if read_sequence[k] == prev_val:
                while k < len(read_sequence) and read_sequence[k] == prev_val:
                    count += 1
                    k += 1
                new_str += f"{count}{prev_val}"
        sequences.append(new_str)
        
    return sequences.pop()
    

        
if __name__ == "__main__":
    print(count_say_sequence(6))

# 1 --> 1
# 2 --> 11
# 3 --> 21
# 4 --> 1211
# 5 --> 111221
# 6 --> 312211