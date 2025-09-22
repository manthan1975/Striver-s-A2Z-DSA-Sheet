# Time complexity : O(n^2)
# Space complexity : O(1)
# Ascending Order
def insertion_sort(arr,n):
    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        while(prev >= 0 and arr[prev] < curr):
            arr[prev+1] = arr[prev]
            prev-=1
        
        arr[prev+1] = curr  # placing the current element in its current position 


def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


if __name__ == "__main__":
    arr = [4, 1, 2, 3, 5]
    n = len(arr)

    insertion_sort(arr, n)
    print_arr(arr, n)




# Descending Order

def insertion_sort(arr,n):
    for i in range(1,n):
        curr = arr[i]
        prev = i-1
        while(prev >= 0 and arr[prev] < curr):
            arr[prev+1] = arr[prev]
            prev-=1
        
        arr[prev+1] = curr  # placing the current element in its current position 


def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


if __name__ == "__main__":
    arr = [4, 1, 2, 3, 5]
    n = len(arr)

    insertion_sort(arr, n)
    print_arr(arr, n)
