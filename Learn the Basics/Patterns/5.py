# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(n):
    for j in range(i,n):
        print('*',end='')
    print()