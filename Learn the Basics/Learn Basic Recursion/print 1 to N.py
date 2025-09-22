# Time complexity = O(n)
# Space complexity = O(n)

def printNum(n):
    if(n==10):
        print(10)
        return
    print(n)
    printNum(n+1)

printNum(1)