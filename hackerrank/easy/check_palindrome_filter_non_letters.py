# Check Palindrome by Filtering Non-Letters
# https://www.hackerrank.com/challenges/check-palindrome-filter-non-letters
# Difficulty: Easy

def isAlphabeticPalindrome(code):
    letters = [c.lower() for c in code if c.isalpha()]
    return letters == letters[::-1]
