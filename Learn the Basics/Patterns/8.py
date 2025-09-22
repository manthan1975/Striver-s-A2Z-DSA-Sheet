# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(n):
    for j in range(0,i):
        print(' ',end='')

    for k in range(i,n):
        print('*',end='')

    for l in range(i,n-1):
        print('*',end='')
    print()