# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

# Optimal approach
# Time Complexity: O(n)
# Space Complexity: O(1)


def nCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element

if __name__ == '__main__':
    r = 5 # row number
    c = 3 # col number
    element = pascalTriangle(r, c)
    print(f"The element at position (r,c) is: {element}")
    


# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

# Naive approach
# Time Complexity: O(n * r)
# Space Complexity: O(1)

def nCr(n, r):
    res = 1

    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(n):
    # printing the entire row n:
    for c in range(1, n+1):
        print(nCr(n-1, c-1), end=" ")
    print()

if __name__ == "__main__":
    n = 5
    pascalTriangle(n)
    

# Optimal approach
# Time Complexity: O(n)
# Space Complexity: O(1)

def pascalTriangle(n):
    ans = 1
    print(ans,end=" ")

    for i in range(1,n):
        ans = ans * (n-i)
        ans = ans // i
        print(ans,end=" ")
    print()


if __name__ == "__main__":
    n = 5
    pascalTriangle(n)



# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

# Naive approach

# Time Complexity: O(n*n*r) ~ O(n3), where n = number of rows, and r = column index.
# Reason: The row loop will run for approximately n times. And generating a row using the naive approach of variation 2 takes O(n*r) time complexity.

# Space Complexity: In this case, we are only using space to store the answer. That is why space complexity can be still considered as O(1).

from typing import *

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []

    #Store the entire pascal's triangle:
    for row in range(1, n+1):
        tempLst = [] # temporary list
        for col in range(1, row+1):
            tempLst.append(nCr(row - 1, col - 1))
        ans.append(tempLst)
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()


# Optimal approach
# Time Complexity: 
# Space Complexity: 

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element

    for col in range(1,row):
        ans = ans * row - col
        ans = ans // col
        ansRow.append(ans)

    return ansRow

def pascalTriangle(n):
    ans = []

    for row in range(1,n+1):
        ans.append(generateRow(row))
    return ans


if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()


# Leetcode solution 

class Solution:
    def generate(self, numRows):
        def generateRow(row):
            val = 1
            row_list = [1]
            for col in range(1, row):
                val = val * (row - col) // col
                row_list.append(val)
            return row_list

        res = []
        for r in range(1, numRows + 1):
            res.append(generateRow(r))
        return res
