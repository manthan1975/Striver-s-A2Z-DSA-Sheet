# Time Complexity: O(n²)
# Space Complexity: O(1)

def pattern(n):
    size = 2*n-1
    for i in range(0,size):
        for j in range(0,size):
            top = i
            left = j
            bottom = size-1-i
            right = size-1-j
            value = min(top,bottom,right,left)
            print(n-value,end="  ")
        print()

pattern(4)