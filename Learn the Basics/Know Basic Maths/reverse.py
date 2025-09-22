n = int(input ("Enter number: "))

reversenum = 0
while(n > 0):
    lastdig = n % 10
    reversenum = (reversenum * 10) + lastdig
    n //= 10
print("reverse number: ",reversenum)

#TIME COMPLEXITY : O(LOGN)
#SPACE COMPLEXITY : O(1)


# leetcode Solution 
def reverse_integer(x):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    rev = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        ld = x % 10
        rev = rev * 10 + ld
        x //= 10

    rev = rev * sign

    if rev < INT_MIN or rev > INT_MAX:
        return 0
    return rev

num = int(input("Enter an integer: "))   # User input lega
result = reverse_integer(num)            # Function call
print("Reversed integer is:", result) 