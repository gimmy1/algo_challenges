def flatten_map(dictionary, nstr="", level=1):
    new_dictionary = {}
    for k, v in dictionary.items():
        if isinstance(v, dict):
            new_dictionary.update(flatten_map(v, nstr + f"{k}/", level+1))
        else:
            ar = (nstr + f"{k}").split("/") if nstr[-1] == "/" else (nstr + f"/{k}").split("/")
            if level < len(ar):
                nstr = "/".join(ar[:level-1])
                # import pdb; pdb.set_trace()
            # import pdb; pdb.set_trace()
            nstr += f"{k}" if nstr[-1] == "/" else f"/{k}"
            new_dictionary[nstr] = v
    return new_dictionary

if __name__ == "__main__":
    dictionary = {
        "a": {
            "b": {
                "c": 12,
                "d": "Hello World",
                "k": "Dude"
            },
            "e": [1,2,3]
            }
        }
    print(flatten_map(dictionary))
