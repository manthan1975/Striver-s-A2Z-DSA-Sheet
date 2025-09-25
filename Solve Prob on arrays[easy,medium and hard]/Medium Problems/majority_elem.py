# Bruteforce approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# def mjElem(nums,n):
#     for val in nums:
#         freq = 0
#         for el in nums:
#             if(el == val):
#                 freq += 1

#                 if(freq > n/2):
#                     return val
                
#     return -1
    
# if __name__ == "__main__":
#     nums = [1,1,2,2,1]
#     n = len(nums)
#     print("The majority element is:", mjElem(nums,n))



# def majorityElement(arr):
#     n = len(arr)

#     for i in range(n):
#         # Selected element is arr[i]
#         cnt = 0
#         for j in range(n):
#             # Counting the frequency of arr[i]
#             if arr[j] == arr[i]:
#                 cnt += 1

#         # Check if frequency is greater than n/2
#         if cnt > (n // 2):
#             return arr[i]

#     return -1

# arr = [2, 2, 1, 1, 1, 2, 2]
# ans = majorityElement(arr)
# print("The majority element is:", ans)


# Better approach
# Time Complexity: O(n log n)
# Space Complexity: O(1) (in-place sort मानकर), otherwise O(log n)
# def majorityElem(arr):
#     n = len(arr)
#     arr.sort()

#     freq = 1
#     ans = arr[0]

#     for i in range(1,n):
#         if arr[i] == arr[i-1]:
#             freq += 1
#         else:
#             freq = 1
#             ans = arr[i]

#         if(freq > n//2):
#             return ans 
        
#     return -1   # if no majority element

# if __name__ == "__main__":
#     arr = [1,1,2,1,2]
#     print(majorityElem(arr))


# Using Hashing
# Time Complexity: O(nLogn + n)
# Space Complexity: O(n)


from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)


# Moore's Voting Algo
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def majorityElement(self, nums):
        freq = 0
        ans = 0
        for i in range(len(nums)):
            if(freq == 0):
                ans = nums[i]

            if(ans == nums[i]):
                freq += 1

            else:
                freq -= 1

        return ans 
