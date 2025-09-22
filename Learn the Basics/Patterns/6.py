# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 6
for i in range(n):
    for j in range(1,n-i):
        print(j, end=' ')
    print()

