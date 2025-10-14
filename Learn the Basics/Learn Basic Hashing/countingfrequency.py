# Using loops
# Time Complexity: O(N*N)
# Space Complexity:  O(N)

def count_frequency(arr):
    n = len(arr)
    visited = [False] * n   # boolean array

    for i in range(n):
        if visited[i]:
            continue

        count = 1
        visited[i] = True   # <- important step

        for j in range(i+1, n):
            if arr[i] == arr[j] and not visited[j]:
                visited[j] = True
                count += 1

        print(f"{arr[i]} occurs {count} times")

arr = [1,2,1,2,3,4]
count_frequency(arr)

# Using map
# Time Complexity: O(N)
# Space Complexity: O(N)

# def count_frequency(arr):
#     freq = {}  

#     for num in arr:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1

#     for value, count in freq.items():
#         print(f"{value} occurs {count} times")


# arr = [1, 2, 3, 1, 2, 1, 4]
# count_frequency(arr)
