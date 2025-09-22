# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5                                #1st
for i in range(65,n+65):
    for j in range(65,i+1):
        print(chr(j), end="")
    print()
                                     #There are two method to solve this
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end='')    #2nd
#     print()