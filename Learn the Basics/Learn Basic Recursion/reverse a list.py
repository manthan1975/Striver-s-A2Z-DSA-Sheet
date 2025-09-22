# Recursive Method
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseArray(arr, start + 1, end - 1)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, 0, n - 1)
    printArray(arr, n)

#  Using an extra array.

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] = arr[i]
    printArray(ans, n)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)

# Space-optimized iterative method

def printarray(arr,n):
    print("The reversed array is: ")
    for i in range(n):
        print(arr[i],end=' ')
    print()

def revarray(arr,n):
    l = 0
    r = n - 1
    while(l < r):
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r-=1
    printarray(arr, n)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    revarray(arr, n)


# Using Library function

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    arr.reverse()


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)
    printArray(arr, n)