# Time Complexity: O(m*n) 
# Space Complexity: O(n)

def printSpiral(mat):
    ans = []
    n = len(mat)        # rows
    m = len(mat[0])     # cols

    srow, scol = 0, 0
    erow, ecol = n-1, m-1

    while srow <= erow and scol <= ecol:

        # Top row
        for j in range(scol, ecol+1):
            ans.append(mat[srow][j])

        # Right col
        for i in range(srow+1, erow+1):
            ans.append(mat[i][ecol])

        # Bottom row
        if srow < erow:   # avoid double row
            for j in range(ecol-1, scol-1, -1):
                ans.append(mat[erow][j])

        # Left col
        if scol < ecol:   # avoid double col
            for i in range(erow-1, srow, -1):
                ans.append(mat[i][scol])

        srow += 1
        scol += 1
        erow -= 1
        ecol -= 1

    return ans


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

ans = printSpiral(mat)
print(ans)
