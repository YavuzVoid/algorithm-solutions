# Count Elements Greater Than Previous Average
# https://www.hackerrank.com/challenges/count-elements-greater-than-previous-average
# Difficulty: Easy

def countResponseTimeRegressions(responseTimes):
    count = 0
    for i in range(1, len(responseTimes)):
        avg = sum(responseTimes[:i]) / i
        if responseTimes[i] > avg:
            count += 1
    return count
