# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 4
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')

    for j in range(i+1):
        print(chr(65+j),end='')

    for j in range(i):
        print(chr(65+i-j-1),end='')          # i - j - 1 ye decreasing index banata hai
    print()