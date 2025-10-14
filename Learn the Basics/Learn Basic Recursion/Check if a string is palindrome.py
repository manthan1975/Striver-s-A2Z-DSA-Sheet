# Using Recursion
# Time Complexity: O(N)
# Space Complexity: O(1)

# def ispalindrome(s,i,n):
#     if(i >= n//2):
#         return True
#     if(s[i] != s[n-i-1]):
#         return False
#     return ispalindrome(s,i+1,n)

# if __name__ == "__main__":
#     naam = "madsam"
#     if(ispalindrome(naam,0,len(naam))):
#         print("The string is palindrome")
#     else:
#         print("The string is not palindrome")

# Leetcode Solution

class Solution(object):
    def isPalindrome(self, s):
        filtered = "".join(ch.lower() for ch in s if ch.isalnum())

        left, right = 0, len(filtered) - 1

        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1

        return True
