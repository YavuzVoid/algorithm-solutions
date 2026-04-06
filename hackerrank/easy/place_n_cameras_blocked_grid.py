def canPlaceSecurityCameras(N, grid):
    cols = set()
    diag1 = set()
    diag2 = set()
    def bt(row):
        if row == N:
            return True
        for col in range(N):
            if grid[row][col] == 1:
                continue
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            if bt(row + 1):
                return True
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
        return False
    return bt(0)
