from typing import List


# start snippet find
def find_longest_word(s: str, d: List[str]) -> str:
    r = ""

    for entry in d:
        if ((len(entry) == len(r) and entry < r)
                or len(entry) > len(r)) and match(s, entry):
            r = entry
    return r
# end snippet find


# start snippet match
def match(s: str, p: str) -> bool:
    i, j = 0, 0
    while i < len(s):
        if j == len(p):
            return True
        if s[i] == p[j]:
            j += 1
        i += 1
    return j == len(p)
# end snippet match
