def count_and_say(Num):
    start = "1"
    st = 0
    nums = [start]
    while st < Num:
        start = count_say_helper(start)
        nums.append(start)
        st += 1
    return nums[Num-1]

def count_say_helper(string):
    idx = 0
    new_string = ""
    while idx < len(string):
        fast = idx
        count = 0
        while fast < len(string) and string[fast] == string[idx]:
            count += 1    
            fast += 1
        new_string += f"{count}{string[idx]}"
        idx = fast
    return new_string


if __name__ == "__main__":
    print(count_and_say(1))