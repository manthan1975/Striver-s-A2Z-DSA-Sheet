# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
space = 2
for i in range(n):
    for j in range(i+1):
        print("*",end='')

    for j in range(2,space * (n-i)):
        print(' ',end='')

    for j in range(i+1):                     # Iss que ko krne k do tarike hai 
        print("*",end='')                    
    print()

for i in range(n):
    for j in range(n-i-1):
        print('*',end='')

    for j in range(space * i+2):              # 1st
        print(" ",end='')

    for j in range(n-i-1):
        print("*",end='')
    print()

# r = 4
# bhaag = 2
# for i in range(r):
#     for j in range(i,r):
#         print('*',end='')

#     for j in range(bhaag * (i+1)):           # 2nd
#         print(' ',end='')

#     for j in range(i,r):
#         print('*',end='')

#     print()