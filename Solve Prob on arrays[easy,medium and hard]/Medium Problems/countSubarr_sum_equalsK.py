# Bruteforce approach
#Time Complexity: O(n^2)
#Space Complexity: O(1)

def countSubarraySum(arr, k):
    n = len(arr)
    count = 0

    for i in range(n):  # starting index
        for j in range(i, n):  # ending index
            sub_sum = 0
            for m in range(i, j+1):  # sum of subarray [i..j]
                sub_sum += arr[m]
            
            if sub_sum == k:
                count += 1
    
    return count


arr = [1, 2, 3]
k = 3
print(countSubarraySum(arr, k))  


# Betterapproach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def countSubarraySum(arr,k):
    n = len(arr)
    count = 0

    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if(sum == k):
                count += 1
    
    return count


if __name__ == "__main__":
    arr = [1,2,3]
    k = 3
    print(countSubarraySum(arr,k))


# Optimal approach
# Time Complexity: O(n)
# Space Complexity: O(n)

def countSubarraySum(arr,k):
    n = len(arr)
    count = 0
    prefixSum = [0] * n

    prefixSum[0] = arr[0]
    for i in range(1,n):
        prefixSum[i] = prefixSum[i-1] + arr[i]

    m = {}
    for j in range(0,n):
        if(prefixSum[j] == k):
            count += 1

        val = prefixSum[j] - k
        if val in m:
            count += m[val]

        if prefixSum[j] not in m:
            m[prefixSum[j]] = 0
        m[prefixSum[j]] += 1
    
    return count



if __name__ == "__main__":
    arr = [1,2,3]
    k = 3
    print(countSubarraySum(arr,k))