# Time complexity : O(n^2)
# space complexity : O(1)
# Ascending Order
def selection_sort(arr,n):
    for i in range(n-1):
        smallest_index = i  # Unsorted part starting 
        for j in range(i+1,n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[i],arr[smallest_index] = arr[smallest_index],arr[i]

def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


if __name__ == "__main__":
    arr = [4, 1, 2, 3, 5]
    n = len(arr)

    selection_sort(arr, n)
    print_arr(arr, n)




# Descending Order

def selection_sort(arr,n):
    for i in range(n-1):
        smallest_index = i  # Unsorted part starting 
        for j in range(i+1,n):
            if arr[j] > arr[smallest_index]:
                smallest_index = j

        arr[i],arr[smallest_index] = arr[smallest_index],arr[i]

def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


if __name__ == "__main__":
    arr = [4, 1, 2, 3, 5]
    n = len(arr)

    selection_sort(arr, n)
    print_arr(arr, n)
