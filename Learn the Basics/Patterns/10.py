# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print('*',end='')
    print()

for i in range(n):
    for j in range(i,n):
        print('*',end='')
    print()