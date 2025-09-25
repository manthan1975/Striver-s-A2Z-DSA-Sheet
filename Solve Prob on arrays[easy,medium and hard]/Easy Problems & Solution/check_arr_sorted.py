# BruteForce approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    ans = isSorted(arr, n)
    if ans:
        print("True")
    else:
        print("False")






# Optimal approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def sort_arr(arr,n):
    for i in range(0,n-1):
            if(arr[i] > arr[i+1]):
                print("The array is not sorted")
                return
            
    print("The array is sorted")

if __name__ == "__main__":
    arr = [1,2,3,4,5,]
    n = len(arr)

    sort_arr(arr,n)


# Leetcode Solution
class Solution(object):
    def check(self, nums):
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False

        return True
