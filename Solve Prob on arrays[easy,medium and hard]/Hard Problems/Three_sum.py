# Bruteforce approach
# Time Complexity: O(N3 * log(no. of unique triplets)), where N = size of the array.
# Reason: Here, we are mainly using 3 nested loops. And inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

# Space Complexity: O(2 * no. of the unique triplets) as we are using a set data structure and a list to store the triplets.

def triplet(arr):
    n = len(arr)
    st = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i] + arr[j] + arr[k] == 0):
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))


    # store the set elements in the answer:
    ans = [list(item) for item in st]
    return ans


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(triplet(arr))


# Better approach
# Time Complexity: O(N2 * log(no. of unique triplets)), where N = size of the array.
# Reason: Here, we are mainly using 3 nested loops. And inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

# Space Complexity: O(2 * no. of the unique triplets) + O(N) as we are using a set data structure and a list to store the triplets and extra O(N) for storing the array elements in another set.


def triplet(arr): 
    n = len(arr)
    st = set()

    for i in range(n):
        tar = -arr[i]
        s = set()

        for j in range(i+1, n):
            third = tar - arr[j]

            if third in s:
                trip = [arr[i], arr[j], third]  # list
                trip.sort()
                st.add(tuple(trip))           # set me tuple add

            s.add(arr[j])

    ans = list(st)
    return ans


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(triplet(arr))



# Optimal approach
# Time Complexity: O(NlogN)+O(N2), where N = size of the array.
# Reason: The pointer i, is running for approximately N times. And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. So the total time complexity will be O(N2). 

# Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So, from that perspective, space complexity can be written as O(1).


def triplet(n, arr):
    ans = []
    arr.sort()
    for i in range(n):
        # remove duplicates:
        if i != 0 and arr[i] == arr[i - 1]:
            continue

        # moving 2 pointers:
        j = i + 1
        k = n - 1
        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                # skip the duplicates:
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return ans



if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    print(triplet(n,arr))