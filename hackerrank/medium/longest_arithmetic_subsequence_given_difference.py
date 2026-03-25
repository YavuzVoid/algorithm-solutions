# Longest Arithmetic Subsequence with Given Difference
# https://www.hackerrank.com/challenges/longest-arithmetic-subsequence-given-diff
# Difficulty: Medium

def findLongestArithmeticProgression(arr, k):
    nums = sorted(set(arr))
    dp = {}
    max_len = 0
    for num in nums:
        dp[num] = dp.get(num - k, 0) + 1
        max_len = max(max_len, dp[num])
    return max_len
