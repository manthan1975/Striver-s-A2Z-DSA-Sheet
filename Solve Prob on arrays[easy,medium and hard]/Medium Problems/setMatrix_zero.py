# Bruteforce approach
# Time Complexity: O(n^3)
# Space Complexity: O(1)

def markRow(matrix,n,m,i):
    for j in range(0,m):
        if(matrix[i][j] != 0):
            matrix[i][j] = -1


def markCol(matrix,n,m,j):
    for i in range(n):
        if(matrix[i][j] != 0):
            matrix[i][j] = -1



def zeroMatrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)



    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix


if __name__ == "__main__":
	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	n = len(matrix)
	m = len(matrix[0])
print(zeroMatrix(matrix,n,m))



# Better approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)


def zeroMatrix(matrix,n,m):
    col = [0] * m      # Column array
    row = [0] * n      # row array
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark ith index of row wih 1:
                row[i] = 1

                # mark jth index of col wih 1:
                col[j] = 1


    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0

    return matrix


if __name__ == "__main__":
	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	n = len(matrix)
	m = len(matrix[0])
	ans = zeroMatrix(matrix, n, m)

	print("The Final matrix is:")
	for row in ans:
	    for ele in row:
	        print(ele, end=" ")
print()



# Optimal approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1

        # Step 1: mark zeros
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: set zeros based on marks
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: handle first row
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        # Step 4: handle first column
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
