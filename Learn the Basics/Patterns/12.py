# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 4
space = 2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')

    for j in range(space * (n-i)):
        print(" ",end='')

    for j in range(1,i+1):
        print(i-j+1,end='')
    print()

# n = 5
# space = 2
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end='')
    
#     for j in range(space * (n-i-1)):
#         print(' ',end='')

#     for j in range(1,i+1):
#         print(i-j+1,end='')
#     print()