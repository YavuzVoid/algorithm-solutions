def findPeakIndex(counts):
    low = 0
    high = len(counts) - 1
    while low < high:
        mid = (low + high) // 2
        if counts[mid] < counts[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
