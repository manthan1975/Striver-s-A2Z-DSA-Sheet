# Time Complexity: O(n²)
# Space Complexity: O(1)

n = 5
num = 1
for i in range(0,n):
    for j in range(0,i+1):
        print(num,end=" ")
        num+=1
    print()