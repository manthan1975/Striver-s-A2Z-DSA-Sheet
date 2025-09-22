# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')

    for j in range(1,i+1):
        print('*',end='')

    for j in range(i+1):
        print('*',end='')
    print()

for i in range(n):
    for j in range(0,i):
        print(' ',end='')

    for j in range(i,n):
        print('*',end='')

    for j in range(i,n-1):
        print('*',end='')
    print()