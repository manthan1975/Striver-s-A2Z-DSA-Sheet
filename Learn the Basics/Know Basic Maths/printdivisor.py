# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)

def print_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    print(divisors)
    return divisors
print_divisors(32)

import math

def print_divisor(n):
    divisors = []
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)

            if n // i != i:
                divisors.append(n//i)
    return sorted(divisors)
print(print_divisor(32))