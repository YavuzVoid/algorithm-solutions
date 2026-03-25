# Subarrays with Given Sum and Bounded Maximum
# https://www.hackerrank.com/challenges/subarrays-given-sum-bounded-maximum
# Difficulty: Hard

def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    count = 0
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] > M:
            i += 1
            continue
        j = i
        while j < n and nums[j] <= M:
            j += 1
        sub = nums[i:j]
        prefix = {0: 1}
        total = 0
        for val in sub:
            total += val
            if (total - k) in prefix:
                count += prefix[total - k]
            prefix[total] = prefix.get(total, 0) + 1
        i = j
    return count
