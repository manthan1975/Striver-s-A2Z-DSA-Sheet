# Bruteforce approach
# Time Complexity: O(n^2)
def pair_sum(arr,n,target):
    ans = []
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i] + arr[j] == target):
                ans.append(i)
                ans.append(j)
                return ans
    return ans

if __name__ == "__main__":
    arr = [2,7,11,15]
    n = len(arr)
    target = 9
    print(pair_sum(arr,n,target))



# Optimal approach(Two Pointer approach)
# Time Complexity: O(n)

def pair_sum(arr,n,target):
    ans = []
    i = 0
    j = n-1
    while(i<j):
        pairSum = arr[i] + arr[j]

        if (pairSum > target):
            j -= 1
        elif (pairSum < target):
            i += 1
        else:
            ans.append(i)
            ans.append(j)
            return ans
        
    return ans


if __name__ == "__main__":
    arr = [2,7,11,15]
    n = len(arr)
    target = 26
    print(pair_sum(arr,n,target))