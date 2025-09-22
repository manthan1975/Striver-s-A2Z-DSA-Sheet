# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(n):
    for j in range(n-i-1):   
        print(' ',end='')

    for k in range(1,i+1):
        print('*',end='')

    for l in range(i+1):
        print('*',end='')
    print()