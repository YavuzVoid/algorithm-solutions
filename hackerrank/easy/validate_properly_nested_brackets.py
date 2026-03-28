def areBracketsProperlyMatched(code_snippet):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for ch in code_snippet:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != matching[ch]:
                return 0
            stack.pop()
    return 1 if not stack else 0
