# Brute Force approach
# TIME COMPLEXITY :  O(LOGN)
# SPACE COMPLEXITY:  O(1)
def count_dig(n):
    count = 0
    while(n>0):
        count+=1
        n//=10
    return count
print(count_dig(13489))

# Optimal appproach
# TIME COMPLEXITY :  O(1)
# SPACE COMPLEXITY:  O(1)
import math
def count_Dig(n):
    cnt = int(math.log10(n) + 1)
    return cnt
print(count_Dig(12345))



import math
n = int(input("Enter number: "))
cnt = int(math.log10(n) + 1)
print(cnt)