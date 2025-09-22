# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
start = 1
for i in range(0,n):
    if (i %  2 == 0):
        start = 1
    else:
        start = 0
    for j in range(i+1):
        print(start,end='')
        start = 1 - start
    print()