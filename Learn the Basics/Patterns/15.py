# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end='')
    print()
