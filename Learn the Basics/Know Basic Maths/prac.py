# Bruteforce approach 
# Time complexity = O(n)
# Space complexity = O(1)
def checkprime(n):
    cnt = 0
    for i in range(1,n+1):
        if(n % i == 0):
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 7
    isPrime = checkprime(n)
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")


# Optimal Approach
# Time complexity = O(srqt(n))
# Space complexity = O(1)

import math

def checkPrime(n):
    cnt = 0

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt = cnt + 1

            if n // i != i:
                cnt = cnt + 1

    if cnt == 2:
        return True
    else: 
        return False

# Main function
def main():
    n = 1483
    isPrime = checkPrime(n)
    if isPrime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

if __name__ == "__main__":
    main()
