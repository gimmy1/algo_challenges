def strStr(haystack, needle):
    if haystack == needle: return 0
    hdx = 0
    needle_len = len(needle)
    while hdx < len(haystack):
        # import pdb; pdb.set_trace()
        try:
            if haystack[hdx] == needle[0]:
                ndx = 0
                h_dx = hdx
                while ndx < needle_len and haystack[h_dx] == needle[ndx]:
                    ndx += 1
                    h_dx += 1
                    if ndx == needle_len:
                        return hdx
            hdx += 1
        except:
            return -1

    return -1



if __name__ == "__main__":
    print(strStr("a", ""))
    print(strStr("heello", "ll"))
