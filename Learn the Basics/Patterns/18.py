# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
k = n
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65 + k - 2 + j),end='')
    print()
    k -= 1







