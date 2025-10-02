# Brute force approach
# Time Complexity: O(n^2) 
# Space Complexity: O(n^2)

def rotate(arr):
    n = len(arr)
    matrix = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[j][n-1-i] = arr[i][j]
    return matrix

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(arr))



# Optimal approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def rotate(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]

    for i in range(n):
        arr[i].reverse()

    return arr

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(arr))