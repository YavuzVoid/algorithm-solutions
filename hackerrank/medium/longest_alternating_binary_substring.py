def longestAlternatingSubstring(s, k):
    n = len(s)
    if n == 0:
        return 0
    best = 0
    for start_char in '01':
        flips = 0
        left = 0
        for right in range(n):
            expected = str((int(start_char) + right) % 2)
            if s[right] != expected:
                flips += 1
            while flips > k:
                exp_left = str((int(start_char) + left) % 2)
                if s[left] != exp_left:
                    flips -= 1
                left += 1
            best = max(best, right - left + 1)
    return best
