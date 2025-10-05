# Bruteforce approach
# Time Complexity: O(n^2) 
# Space Complexity: O(1)

def countInversion(arr):
    n = len(arr)
    invCount = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i] > arr[j]):
                invCount += 1
    return invCount

    
arr = [1,3,5,10,2,6,8,9]
print("Inversion count:",countInversion(arr))

# Optimal approach
# Time Complexity: O(nlogn)
# Space Complexity: O(n)


def merge(arr,st,mid,end):
    temp = []
    i = st
    j = mid + 1
    invCount = 0
    while(i <= mid and j <= end):
        if(arr[i] <= arr[j]):
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            invCount += (mid - i + 1)

    while(i <= mid):
        temp.append(arr[i])
        i += 1

    while(j <= end):
        temp.append(arr[j])
        j += 1

    for idx in range(len(temp)):
        arr[idx + st] = temp[idx]

    return invCount

    
def mergeSort(arr,st,end):
    if(st < end):
        mid = st + (end-st) // 2
        leftInvCount = mergeSort(arr,st,mid)
        rightInvCount = mergeSort(arr,mid+1,end)

        invCount = merge(arr,st,mid,end)

        return leftInvCount + rightInvCount + invCount
    
    return 0


if __name__ == "__main__":
    arr = [1,3,5,10,2,6,8,9]
    ans = mergeSort(arr,0,len(arr) - 1)
    print("Inversion count:",ans)




