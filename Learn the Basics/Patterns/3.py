# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 6
for i in range(0,n):
    for j in range(1,i+1):
        print(j,end='')
    print()