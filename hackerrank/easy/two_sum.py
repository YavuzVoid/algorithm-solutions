def findTaskPairForSlot(taskDurations, slotLength):
    seen = {}
    for i, d in enumerate(taskDurations):
        comp = slotLength - d
        if comp in seen:
            return [seen[comp], i]
        seen[d] = i
    return [-1, -1]
