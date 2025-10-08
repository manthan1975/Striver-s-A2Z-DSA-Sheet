# Bruteforce approach
# Time Complexity: O(nlogn) + O(2n)
# Space Complexity: O(n)

def mergeOverlappingSubInterval(arr):
    n = len(arr)
    arr.sort()
    ans = []

    for i in range(0,n):
        start,end = arr[i][0],arr[i][1]

        # Skip all the merged intervals:
        if ans and end <= ans[-1][1]:
            continue

        for j in range(i+1,n):
            if(arr[j][0] <= end):
                end = max(end,arr[j][1])
            else:
                break

        ans.append([start,end])

    return ans

if __name__ == "__main__":
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]] 
    print(mergeOverlappingSubInterval(arr))


# Optimal approach
# Time Complexity: 
# Space Complexity:


def mergeOverlappingSubInterval(arr):
    n = len(arr)
    arr.sort()
    ans = []

    for i in range(0,n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])

    return ans

if __name__ == "__main__":
    arr = [[1, 3], [8, 10], [2, 6], [15, 18]] 
    print(mergeOverlappingSubInterval(arr))
