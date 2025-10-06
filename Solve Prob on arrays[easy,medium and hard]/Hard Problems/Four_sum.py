# Optimal approach
# Time Complexity: O(N3), where N = size of the array.
# Reason: Each of the pointers i and j, is running for approximately N times. And both the pointers k and l combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N3). 

# Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).

def fourSum(nums,target):
    n = len(nums) 
    ans = []

    nums.sort()

    for i in range(n):
       
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            # avoid the duplicates while moving j:
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # 2 pointers:
            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1

                    # skip the duplicates:
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1

    return ans


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(fourSum(nums,target))