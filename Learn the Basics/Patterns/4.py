# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(0,n):
    for j in range(i+1):
        print(i+1,end=' ')
    print()