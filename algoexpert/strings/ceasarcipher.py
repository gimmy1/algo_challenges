import string
alphabet_list = list(string.ascii_lowercase)
alphabet_dict = {i+1: v for i, v in enumerate(alphabet_list)}
inverse_alphabet = {val: key for key, val in alphabet_dict.items()}

def ceasar_cipher(phrase, key):
    ciphered = ""
    for p in phrase:
        # import pdb; pdb.set_trace()
        num = inverse_alphabet[p] + key
        if num > 26:
            new_value = num % 26
        else:
            new_value = num
        ciphered += alphabet_dict[new_value]
    return ciphered

if __name__ == "__main__":
    print(ceasar_cipher("xyz", 2))



