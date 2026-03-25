# Find the Smallest Missing Positive Integer
# https://www.hackerrank.com/challenges/find-smallest-missing-positive-integer
# Difficulty: Easy

def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    for i in range(n):
        while 1 <= orderNumbers[i] <= n and orderNumbers[orderNumbers[i] - 1] != orderNumbers[i]:
            idx = orderNumbers[i] - 1
            orderNumbers[i], orderNumbers[idx] = orderNumbers[idx], orderNumbers[i]
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1
    return n + 1
