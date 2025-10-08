# Bruteforce approach
# Time Complexity: O(n^3)
# Space Complexity: O(1)


def maxProdArr(arr,n):
    maxi = float('-inf')
    for i in range(0,n-1):
        for j in range(i+1,n):
            prod = 1
            for k in range(i,j+1):
                prod = prod * arr[k]

            maxi = max(maxi,prod)

    return maxi
if __name__ == "__main__":
    arr = [1, 2, -3, 0, -4, -5]
    n = len(arr)
    print("The maximum product subarray:",maxProdArr(arr,n))


# Better approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def maxProdArr(arr):
    maxi = float('-inf')
    for i in range(len(arr) - 1):
        prod = 1
        for j in range(i+1,len(arr)):
            prod *= arr[j]

        maxi = max(maxi,prod)

    return maxi


if __name__ == "__main__":
    arr = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:",maxProdArr(arr))

# Optimal approach 1
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxProdArr(arr):
    n = len(arr)
    pre = 1
    suff = 1
    ans = float('-inf')


    for i in range(len(arr)):
        if(pre == 0):
            pre = 1
        if(suff == 0):
            suff = 1

        pre *= arr[i]
        suff *= arr[n - i - 1]
        ans = max(ans, max(pre, suff))

    return ans

if __name__ == "__main__":
    arr = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:",maxProdArr(arr))




# Optimal approach 2
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxProductSubArray(nums):
    prod1 = nums[0]
    prod2 = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        temp = max(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod1 = temp

        result = max(result, prod1)

    return result

if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", maxProductSubArray(nums))

