def findFirstOccurrence(nums, target):
    low = 0
    high = len(nums) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            result = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
