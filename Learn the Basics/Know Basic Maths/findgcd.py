# GCD : Greatest common divisor 
# HCF : Highest common factor

# Brute force approach
# Time Complexity: O(min(n1,n2))
# Space Complexity: O(1)


# def find_gcd(n1,n2):
#     gcd = 1

#     for i in range(1,min(n1,n2)):
#         if(n1 % i == 0 and n2 % i == 0):
#             gcd = i
#     return gcd

# print(find_gcd(9,12))



# Optimal approach 
# Time Complexity: O(min(n1,n2))
# Space Complexity: O(1)


def find_gcd(n1,n2):
    while(n1 > 0 and n2 > 0):
        if (n1 > n2):
            n1 = n1 % n2
        else:
            n2 = n2 %  n1

        if(n1 == 0):
            return n2
        else:
            return n1

print(find_gcd(52,10))



# Better approach
# Time Complexity: O(min(n1,n2))
# Space Complexity: O(1)

# def find_gcd(n1,n2):
#     gcd = 1
#     for i in range(min(n1,n2),0,-1):
#         if n1 % i == 0 and n2 % i == 0:
#             return i
        
#     return 1
# print(find_gcd(20,15))


