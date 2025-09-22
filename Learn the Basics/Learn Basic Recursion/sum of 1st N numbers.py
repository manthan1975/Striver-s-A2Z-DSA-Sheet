#Using for loop

# n = 5
# sum = 0
# for i in range(n+1):
#     sum = sum + i
    
# print(sum)

# Using the formula

# sum = int(input("Enter number: "))

# sum = sum * (sum + 1)/2

# print(sum)

# Using Recursion
# Parameterised way

def func(i,sum):
    if(i<1):
        print(sum)
        return
    func(i-1,sum + i)

n = int(input("Enter n: "))
func(n,0)



# Functional way
# def sum(n):
#     if(n == 0):
#         return 0
#     return n + sum(n-1)
# print(sum(3))