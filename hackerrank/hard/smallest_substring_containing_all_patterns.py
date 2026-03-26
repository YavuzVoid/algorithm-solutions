# Smallest Substring Containing All Patterns
# https://www.hackerrank.com/challenges/smallest-substring-containing-all-patterns
# Difficulty: Hard

def findSmallestSubstringWindow(patterns, S):
    if not patterns or not S:
        return [-1, -1]
    unique = list(set(patterns))
    n = len(S)
    m = len(unique)
    pos = {}
    for p in unique:
        starts = []
        i = 0
        while i <= n - len(p):
            idx = S.find(p, i)
            if idx == -1:
                break
            starts.append(idx)
            i = idx + 1
        if not starts:
            return [-1, -1]
        pos[p] = starts
    best = None
    ptrs = {p: 0 for p in unique}
    while True:
        lo = n
        hi = 0
        min_p = None
        min_start = n
        for p in unique:
            s = pos[p][ptrs[p]]
            e = s + len(p) - 1
            if s < min_start:
                min_start = s
                min_p = p
            lo = min(lo, s)
            hi = max(hi, e)
        if best is None or (hi - lo) < (best[1] - best[0]):
            best = [lo, hi]
        ptrs[min_p] += 1
        if ptrs[min_p] >= len(pos[min_p]):
            break
    return best
