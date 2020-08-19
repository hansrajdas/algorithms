def char_to_index(c):
    return ord(c) - ord('a')

def has_all_chars_unique(string):
    mask = 0
    for c in string:
        print(char_to_index(c))
        if mask & (1 << char_to_index(c)):
            return False
        mask |= 1 << char_to_index(c)
    return True

assert has_all_chars_unique('abc') == True
assert has_all_chars_unique('aac') == False
assert has_all_chars_unique('abb') == False
assert has_all_chars_unique('cbc') == False
assert has_all_chars_unique('bbc') == False
