from collections import defaultdict
def run_length_encoding(string):
    # AAAAAAAAAAAAABBCCCCDD
    encoding = ""
    counter = 0
    idx = 0
    while idx < len(string):
        if idx == len(string) - 1:
            encoding += f"1{string[idx]}"
            return encoding

        jdx = idx + 1
        counter += 1
        while jdx < len(string):
            if string[jdx] != string[idx]:
                break
            if counter == 9:
                break
            counter += 1
            jdx += 1
        encoding += f"{counter}{string[idx]}"
        counter = 0
        idx = jdx
    return encoding

        

if __name__ == "__main__":
    print(run_length_encoding("AAAAAAAAABBCCCCDD"))
    print(run_length_encoding("ABABAAAAAAAAAAB"))