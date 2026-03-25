# Merge and Sort Intervals
# https://www.hackerrank.com/challenges/merge-and-sort-intervals
# Difficulty: Easy

def mergeHighDefinitionIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged
