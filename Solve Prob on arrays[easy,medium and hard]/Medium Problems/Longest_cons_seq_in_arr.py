# Bruteforce approach
# Time Complexity: O(n^2)
# Space Complexity: (1)

def linearSearch(a, num):
    n = len(a)  # size of array
    for i in range(n):
        if a[i] == num:
            return True
    return False


def consSeq(arr):
    n = len(arr)
    longest = 1
    for i in range(0,n):
        x = arr[i]
        cnt = 1

        while linearSearch(arr, x + 1):
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest


if __name__ == "__main__":
    arr = [100,200,1,2,3,4]
    print(consSeq(arr))


# Better approach
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

def consSeq(arr):
    n = len(arr)
    if n == 0:
        return 0
    

    arr.sort()
    lastSmaller = float('-inf')
    cnt = 0
    longest = 1

    for i in range(0,n):
        if(arr[i] - 1 == lastSmaller):
            cnt += 1
            lastSmaller = arr[i]

        elif(arr[i] != lastSmaller):
            cnt = 1
            lastSmaller = arr[i]

        longest = max(longest,cnt)
    return longest


if __name__ == "__main__":
    arr = [100,200,1,2,3,4]
    print(consSeq(arr))


# Optimal approach
# Time Complexity: O(n)
# Space Complexity: O(n)

def consSeq(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    longest = 1
    st = set()

    for i in range(n):
        st.add(arr[i])

    
    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1

            longest = max(longest, cnt)

    return longest

if __name__ == "__main__":
    arr = [100,200,1,2,3,4]
    print(consSeq(arr))
