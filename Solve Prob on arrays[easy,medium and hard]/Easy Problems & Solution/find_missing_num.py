# Bruteforce approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def find_missing(arr,n):
    for i in range(1,n+1):
        flag = 0
        for j in range(len(arr)):
            if arr[j] == i:
                flag = 1
                break

        if flag == 0:
            return i

    return -1

def main():
    n = 5
    arr = [1, 2, 4, 5]
    ans = find_missing(arr, n)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


# Better approach (Using Hashing)
# Time Complexity: O(n)
# Space Complexity: O(n)

def find_missing(arr,n):
    hash = [0] * (n+1)

    for i in range(n-1):
        hash[arr[i]] += 1

    for i in range(1,n+1):
        if hash[i] == 0:
            return i
    
    return -1

def main():
    n = 5
    arr = [1, 2, 4, 5]
    ans = find_missing(arr, n)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()



# Optimal approach 1 (Using Summation)
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_missing(arr,n):
    summation = (n * (n + 1)) // 2

    s2 = sum(arr)

    missingNum = summation - s2
    return missingNum

def main():
    n = 5
    arr = [1, 2, 4, 5]
    ans = find_missing(arr, n)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()



# Optimal approach 2 (Using XOR)
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_missing(arr, n):
    xor1 = 0
    xor2 = 0

    for i in range(n - 1):
        xor2 = xor2 ^ arr[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ n  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


def main():
    n = 5
    arr = [1, 2, 4, 5]
    ans = find_missing(arr, n)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()
