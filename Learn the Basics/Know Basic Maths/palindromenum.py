# Time Complexity: O(Logn)
# Space Complexity: O(1)

n = int(input("Enter a number: "))
revNum = 0
duplicate_num = n

while(n>0):
    lastdig = n % 10
    revNum = (revNum * 10) + lastdig
    n //= 10

if (duplicate_num == revNum):
    print("The number is Palindrome")
else:
    print("The number is not Palindrome")

# Leetcode solution
class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        revNum = 0
        dup_num = x
        
        while x > 0:
            lastdig = x % 10
            revNum = (revNum * 10) + lastdig
            x //= 10
        
        return dup_num == revNum
