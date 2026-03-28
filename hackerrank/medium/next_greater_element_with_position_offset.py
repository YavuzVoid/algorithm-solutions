def findNextGreaterElementsWithDistance(readings):
    n = len(readings)
    result = [[-1, -1]] * n
    stack = []
    for i in range(n):
        while stack and readings[stack[-1]] < readings[i]:
            idx = stack.pop()
            result[idx] = [readings[i], i - idx]
        stack.append(i)
    return result
