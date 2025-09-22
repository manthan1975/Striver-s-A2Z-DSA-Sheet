# Time complexity : O(n^2)
# space complexity : O(1)
# Ascending Order

# Normal approach
def bubble_sort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def print_arr(arr,n):
    for i in range(1, n+1):
        print(i,end=' ')
    print()

if __name__ == "__main__":
    arr = [4,1,2,3,5]
    n = len(arr)

    bubble_sort(arr,n)
    print_arr(arr,n)


# Time complexity : O(n^2) for the worst and average cases and O(N) for the best case.
# space complexity : O(1)

# Optimized approach
def bubble_sort(arr, n):
    for i in range(n):
        swapped = False  
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True   
        if not swapped:   
            break


def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


if __name__ == "__main__":
    arr = [4, 1, 2, 3, 5]
    n = len(arr)

    bubble_sort(arr, n)
    print_arr(arr, n)












# Descending Order
def bubble_sort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:   # descending order
                arr[j], arr[j+1] = arr[j+1], arr[j]

def print_arr(arr,n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

if __name__ == "__main__":
    arr = [4,1,2,3,5]
    n = len(arr)

    bubble_sort(arr,n)
    print_arr(arr,n)
