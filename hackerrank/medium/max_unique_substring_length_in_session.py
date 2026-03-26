# Max Unique Substring Length in a Session
# https://www.hackerrank.com/challenges/max-unique-substring-length-in-session
# Difficulty: Medium

def maxDistinctSubstringLengthInSessions(sessionString):
    sessions = sessionString.split('*')
    max_len = 0
    for s in sessions:
        seen = {}
        left = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)
    return max_len
