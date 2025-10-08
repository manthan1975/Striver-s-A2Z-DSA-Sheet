# Bruteforce approach
# Time Complexity: O(n+m) + O(n+m)
# Space Complexity: O(n+m)


def mergeArr(arr1,arr2,n,m):
    arr3 = [0] * (n + m)
    left = 0
    right = 0
    index = 0

    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1

    # If right pointer reaches the end:
    while left < n:
        arr3[index] = arr1[left]
        left += 1
        index += 1

    # If left pointer reaches the end:
    while right < m:
        arr3[index] = arr2[right]
        right += 1
        index += 1

    # Fill back the elements from arr3[]
    # to arr1[] and arr2[]:
    for i in range(n + m):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]

    return arr1,arr2

if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    print(mergeArr(arr1,arr2,n,m))


# Optimal approach
# Time Complexity:O(min(n, m)) + O(n*logn) + O(m*logm), where n and m are the sizes of the given arrays.
# Reason: O(min(n, m)) is for swapping the array elements. And O(n*logn) and O(m*logm) are for sorting the two arrays.
# Space Complexity: O(1)

def mergeArr(arr1,arr2,n,m):
    # Declare 2 pointers:
    left = n - 1
    right = 0

    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    arr1.sort()
    arr2.sort()
    return arr1,arr2


if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    print(mergeArr(arr1,arr2,n,m))