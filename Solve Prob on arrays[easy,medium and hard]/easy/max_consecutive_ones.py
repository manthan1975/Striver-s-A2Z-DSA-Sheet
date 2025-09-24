# Leetcode Solution
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)
        return maxi
    

def find_max_consecutive_ones(nums):
    cnt = 0       # current consecutive 1s count
    maxi = 0      # maximum consecutive 1s found so far
    
    for num in nums:
        if num == 1:
            cnt += 1      # agar 1 mila → current count badhao
        else:
            cnt = 0       # agar 0 mila → current count reset
        maxi = max(maxi, cnt)  # maximum update karo
    
    return maxi

# Example usage:
nums = [1, 1, 0, 1, 1, 1, 0, 1]
result = find_max_consecutive_ones(nums)
print("Maximum consecutive ones:", result)
