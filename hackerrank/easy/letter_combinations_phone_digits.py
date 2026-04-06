def minTasksToCancelForNoConflict(digits):
    if not digits:
        return []
    mapping = {
        '0': '0', '1': '1', '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    result = []
    def bt(i, path):
        if i == len(digits):
            result.append(path)
            return
        for ch in mapping[digits[i]]:
            bt(i + 1, path + ch)
    bt(0, '')
    return sorted(result)
