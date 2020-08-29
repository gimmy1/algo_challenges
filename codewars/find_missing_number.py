def find_number(start, stop, string):
    dictionary_range = dict(zip(range(start, stop+1),
                                [False] * len(range(start, stop+1))))
    
    i = 0
    while i < len(string):
        number = ""
        number = string[i]
        while int(number) in range(start, stop+1):
            if int(number) not in range(start, stop+1):
                while i < len(string) and int(number) not in range(start, stop+1):
                    i += 1
                    number += string[i]
            
            if dictionary_range[int(number)]:
                while i < len(string) and int(number) not in range(start, stop+1):
                    i += 1
                    number += string[i]
            
            if not dictionary_range[int(number)]:
                dictionary_range[int(number)] = True
        i += 1
    
    return [key for key, val in dictionary_range.items() if val is False]


if __name__ == "__main__":
    print(find_number(1, 21, "2198765123416171890101112131415"))