# Time complexity = O(n)
# Space complexity = O(n)

def printNum(n):
    if(n==1):
        print(1)
        return
    print(n)
    printNum(n-1)

printNum(4)