# Check for Non-Identical String Rotation
# https://www.hackerrank.com/challenges/check-non-identical-string-rotation
# Difficulty: Easy

def isNonTrivialRotation(s1, s2):
    if s1 == s2:
        return False
    return len(s1) == len(s2) and s2 in s1 + s1
