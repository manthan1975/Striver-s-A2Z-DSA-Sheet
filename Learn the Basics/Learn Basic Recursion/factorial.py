# Using Iteration

# n = 3
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)


# Using Recursion

def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)

print(factorial(3))