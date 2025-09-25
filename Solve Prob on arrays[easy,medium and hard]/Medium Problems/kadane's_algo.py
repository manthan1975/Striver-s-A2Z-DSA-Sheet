# Maximum Subarr Sum - BruteFroce approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
n = 5
arr = [1,2,3,4,5]
INT_MIN = -2**31
maxSum = INT_MIN

for st in range(0,n):
    currSum = 0
    for end in range(st,n):
        currSum += arr[end]
        maxSum = max(currSum,maxSum)


print("Maximum Subarr sum: ",maxSum)


# Kadane's Algorithm
def maxSub_arr(arr,n):
    currSum = 0
    INT_MIN = -2**31
    maxSum = INT_MIN

    for i in range(0,n):
        currSum += arr[i]
        maxSum = max(currSum,maxSum)

        if (currSum < 0):
            currSum = 0

    return maxSum


if __name__ == "__main__":
    n = 5
    arr = [1,2,3,4,5]
    print(maxSub_arr(arr,n))
    

# Leetcode Solution
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def maxSubArray(self, nums):
        currSum = 0
        INT_MIN = -2**31
        maxSum = INT_MIN

        for val in nums:
            currSum += val
            maxSum = max(currSum,maxSum)

            if (currSum < 0):
                currSum = 0

        return maxSum
        """
        :type nums: List[int]
        :rtype: int
        """
        