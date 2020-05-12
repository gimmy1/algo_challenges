def wave(people):
    idx = 0
    waved = []
    while idx < len(people):
        front = people[:idx]
        if people[:idx+1][-1] == " ":
            while people[:idx+1][-1] == " ":
                if idx > len(people):
                    return waved
                front += " "
                idx += 1
        wave = people[:idx+1][-1]
        end = people[idx+1:]
        waved.append(front+wave.upper()+end)
        idx += 1
    return waved
    
if __name__ == "__main__":
    print(wave(" gap "))