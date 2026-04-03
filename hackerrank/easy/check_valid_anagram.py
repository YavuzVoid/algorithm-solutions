def isAnagram(s, t):
    if len(s) != len(t):
        return 0
    from collections import Counter
    return 1 if Counter(s) == Counter(t) else 0
