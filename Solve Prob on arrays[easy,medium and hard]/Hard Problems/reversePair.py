# Bruteforce approach
# Time Complexity: O(n^2) 
# Space Complexity: O(1)

def countPairs(arr):
    cnt = 0
    n = len(arr)

    for i in range(0,n):
        for j in range(i,n):
            if(arr[i] > 2*arr[j]):
                cnt += 1

    return cnt


if __name__ == "__main__":
    arr = [4,1,2,3,1]
    print("The number of reverse pair is:",countPairs(arr))





















# Optimal approach
# Time Complexity: O(2N*logN), where N = size of the given array.
# Reason: Inside the mergeSort() we call merge() and countPairs() except mergeSort() itself. Now, inside the function countPairs(), though we are running a nested loop, we are actually iterating the left half once and the right half once in total. That is why, the time complexity is O(N). And the merge() function also takes O(N). The mergeSort() takes O(logN) time complexity. Therefore, the overall time complexity will be O(logN * (N+N)) = O(2N*logN).

# Space Complexity: O(N), as in the merge sort We use a temporary array to store elements in sorted order.
def merge(arr,st,mid,end):
    temp = []
    i = st 
    j = mid + 1

    while(i <= mid and j <= end):
        if(arr[i] <= arr[j]):
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while(i <= mid):
        temp.append(arr[i])
        i += 1

    while(j <= end):
        temp.append(arr[j])
        j += 1

    for idx in range(len(temp)):
        arr[idx + st] = temp[idx]
        

def countPairs(arr,st,mid,end):
    cnt = 0
    right = mid + 1
    for i in range(st,mid+1):
        while(right <= end and arr[i] > 2*arr[right]):
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def merge_sort(arr,st,end):
    cnt = 0
    if(st < end):
        mid = st + (end-st)//2

        cnt += merge_sort(arr,st,mid)        # Left Half
        cnt += merge_sort(arr,mid+1,end)     # Right Half
        cnt += countPairs(arr,st,mid,end)
        merge(arr,st,mid,end)
    return cnt


def team(skill,n):
    return merge_sort(skill,0,n-1)

if __name__ == "__main__":
    a = [4, 1, 2, 3, 1]
    n = 5
    cnt = team(a, n)
    print("The number of reverse pair is:", cnt)