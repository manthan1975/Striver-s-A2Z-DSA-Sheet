# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
space = 2
for i in range(n):
    for j in range(i,n):
        print('*',end='')

    for j in range(space * i):
        print(' ', end='')

    for j in range(i,n):                
        print("*",end='')
    print()

for i in range(n):
    for j in range(0,i+1):
        print('*',end='')

    for j in range(2,space * (n-i)):
        print(' ',end='')

    for j in range(i+1):
        print("*",end='')
    print()
