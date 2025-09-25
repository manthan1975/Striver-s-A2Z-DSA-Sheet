# Time Complexity: O(n)
# Space Complexity: O(1)   
# Leetcode Solution
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1                        # first element hamesha unique hoga
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k 
    


# Optimal approach    
def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # first element  hamesha unique hoga
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4]
    k = removeDuplicates(arr)
    print("Unique count:", k)
    print("Modified array:", arr[:k])





# Bruteforce Approach
# Time Complexity: O(n)
# Space Complexity: O(n)

def removeduplicates(arr,n):
    st = set()
    for i in range(0,n):
        st.add(arr[i])

    k = len(st)
    j = 0

    for x in st:
        arr[j] = x
        j += 1 
    return k 

if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3]
    n = len(arr)
    k = removeduplicates(arr,n)
    print("The array after removing duplicates elem is: ")
    for i in range(0,k):
        print(arr[i],end=' ')


