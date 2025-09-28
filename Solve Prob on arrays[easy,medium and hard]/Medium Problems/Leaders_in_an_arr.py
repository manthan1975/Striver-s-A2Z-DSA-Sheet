# Bruteforce approach
# Time Complexity: O(n^2)
# Space Complexity: O(N) { There is no extra space being used in this approach. But, a O(N) of space for ans array will be used in the worst case }.

def findLeaders(arr,n):
    ans = []
    for i in range(0,n):
        leader = True

        for j in range(i+1,n):
            if(arr[j] > arr[i]):
                leader = False
                break

        if leader:
            ans.append(arr[i])

    return ans
 

if __name__ == '__main__':
    n = 6
    arr = [10, 22, 12, 3, 0, 6]
    print(findLeaders(arr,n))


# Optimal approach
# Time Complexity: O(n)
# Space Complexity: O(N) { There is no extra space being used in this approach. But, a O(N) of space for ans array will be used in the worst case }.

def findLeaders(arr,n):
    ans = []
    INT_MIN = -2**31
    maxi = INT_MIN

    for i in range(n-1,-1,-1):
        if(arr[i] > maxi):
            ans.append(arr[i])

        maxi = max(maxi,arr[i])

    ans.sort()
    return ans

if __name__ == '__main__':
    n = len(arr)
    arr = [10, 22, 12, 3, 0, 6]
    print(findLeaders(arr,n))