def countAffordablePairs(prices, budget):
    count = 0
    left = 0
    right = len(prices) - 1
    while left < right:
        if prices[left] + prices[right] <= budget:
            count += right - left
            left += 1
        else:
            right -= 1
    return count
