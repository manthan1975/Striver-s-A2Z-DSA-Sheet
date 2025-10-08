# Bruteforce approach
# Time Complexity: O(n^3)
# Space Complexity: O(1)

def subarraysWithXorK(a,k):
    n = len(a) 
    cnt = 0

    for i in range(n):
        for j in range(i, n):

            # calculate XOR of all elements:
            xorr = 0
            for K in range(i, j + 1):
                xorr = xorr ^ a[K]

            # check XOR and count:
            if (xorr == k):
                cnt += 1

    return cnt

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6
    ans = subarraysWithXorK(a, k)
    print("The number of subarrays with XOR k is:", ans) 

# Better approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def subarraysWithXorK(a,k):
    n = len(a) 
    cnt = 0

    for i in range(n):
        xorr = 0
        for j in range(i, n):

            # step 2: calculate XOR of all elements:
            xorr = xorr ^ a[j]
            if (xorr == k):
                cnt += 1

    return cnt

        

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6
    ans = subarraysWithXorK(a, k)
    print("The number of subarrays with XOR k is:", ans) 


# Optimal approach
# Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
# Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array. Point to remember for unordered_map in the worst case, the searching time increases to O(N), and hence the overall time complexity increases to O(N2). 

# Space Complexity: O(n)

def subarraysWithXorK(a, k):
    n = len(a)
    xr = 0
    mpp = {0: 1}  # prefix XOR count
    cnt = 0

    for i in range(n):
        xr = xr ^ a[i]

        # XOR we need
        x = xr ^ k
        cnt += mpp.get(x, 0)

        # update prefix XOR frequency
        mpp[xr] = mpp.get(xr, 0) + 1

    return cnt


if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6
    ans = subarraysWithXorK(a, k)
    print("The number of subarrays with XOR k is:", ans)






