# Time Complexity: O(Logn)
# Space Complexity: O(1)

n = int(input("Enter a number: "))
sum_num = 0
revNum = 0
duplicate_num = n

while(n>0):
    lastdig = n % 10
    revNum = (revNum * 10) + lastdig
    n //= 10
    sum_num = sum_num + (lastdig ** 3)
if (sum_num == duplicate_num):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
