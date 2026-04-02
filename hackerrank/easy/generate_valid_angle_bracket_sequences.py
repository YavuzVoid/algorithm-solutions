def generateAngleBracketSequences(n):
    result = []
    def bt(s, open_count, close_count):
        if open_count == n and close_count == n:
            result.append(s)
            return
        if open_count < n:
            bt(s + '<', open_count + 1, close_count)
        if close_count < open_count:
            bt(s + '>', open_count, close_count + 1)
    bt('', 0, 0)
    return result
