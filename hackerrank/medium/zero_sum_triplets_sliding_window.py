def findZeroSumTripletsInWindow(readings, windowSize):
    n = len(readings)
    result = set()
    for i in range(n - 2):
        end = min(i + windowSize, n)
        window = readings[i:end]
        window_sorted = sorted(window)
        m = len(window)
        for a in range(m - 2):
            if a > 0 and window_sorted[a] == window_sorted[a - 1]:
                continue
            lo = a + 1
            hi = m - 1
            while lo < hi:
                s = window_sorted[a] + window_sorted[lo] + window_sorted[hi]
                if s == 0:
                    result.add((window_sorted[a], window_sorted[lo], window_sorted[hi]))
                    lo += 1
                    hi -= 1
                    while lo < hi and window_sorted[lo] == window_sorted[lo - 1]:
                        lo += 1
                    while lo < hi and window_sorted[hi] == window_sorted[hi + 1]:
                        hi -= 1
                elif s < 0:
                    lo += 1
                else:
                    hi -= 1
    return [list(t) for t in result]
