# Time Complexity: O(logn)
# Space Complexity: O(1)
def binary_exponentiation(base,expo):
    binForm = expo
    if(expo < 0):
        base = 1/base
        binForm = -binForm


    ans = 1

    while(binForm > 0):
        if(binForm % 2 == 1):
            ans *= base
            
        base *= base 
        binForm //= 2

    return ans


if __name__ == "__main__":
    base = 3
    expo = 2                                  
    print(binary_exponentiation(base,expo))