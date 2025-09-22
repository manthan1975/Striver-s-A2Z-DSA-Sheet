# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
for i in range(n):          # i = row    range means = [start,stop,step]
    for j in range(n):      # j = column
        print('*',end='')
    print()

