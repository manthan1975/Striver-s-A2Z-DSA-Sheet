# Bruteforce approach
# Time Complexity: O(n! * nlogn)
# Space Complexity: O(n!)

import itertools

def next_permutation(arr):
    # Step 1: generate all permutations
    perms = sorted(set(itertools.permutations(arr)))
    
    # Step 2: find current permutation index
    idx = perms.index(tuple(arr))
    
    # Step 3: return next permutation (or first if last)
    if idx == len(perms) - 1:
        return list(perms[0])   # wrap around
    else:
        return list(perms[idx + 1])


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(next_permutation(arr)) 





# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_nextPermutation(arr):
    pivot = -1
    n = len(arr)

    for i in range(n-2,-1,-1):
        if(arr[i] < arr[i+1]):
            pivot = i
            break


    if(pivot == -1):
        arr.reverse()
        return arr
    
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break


    i = pivot+1
    j = n-1
    while(i <= j):
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1

    return arr

if __name__ == "__main__":
    arr = [1,2,3]
    print(find_nextPermutation(arr))