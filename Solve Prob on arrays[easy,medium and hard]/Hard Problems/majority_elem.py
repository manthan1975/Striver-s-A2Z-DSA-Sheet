# Bruteforce approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def majority_elem(nums):
    n = len(nums)
    ls = []

    for i in range(0, n):
        if len(ls) == 0 or nums[i] not in ls:
            cnt = 0
            for j in range(0, n):
                if nums[j] == nums[i]:
                    cnt += 1

            if cnt > (n // 3):
                ls.append(nums[i])

        if len(ls) == 2:
            break

    return ls


if __name__ == "__main__":
    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print("The majority elem are:", majority_elem(nums))


# Better approach
# Time Complexity: O(n log n) (due to sort) || Without sort() =  TC = O(n)
# Space Complexity: O(n)

def majority_elem(arr):
    ls = []
    freq = {}
    n = len(arr)
    mini = n // 3 + 1

    for i in range(n):
        # initialize key if not present
        if arr[i] not in freq:
            freq[arr[i]] = 0
        freq[arr[i]] += 1

        # check once when count crosses threshold
        if freq[arr[i]] == mini:
            ls.append(arr[i])

        if len(ls) == 2:
            break

    arr.sort()
    return ls


if __name__ == "__main__":
    arr = [1, 1, 1, 3, 3, 2, 2, 2]
    print("The majority elem are:", majority_elem(arr))


# Optimal approach
# Time Complexity: O(n)
# Space Complexity: O(1)

def majorityElement(nums):
    n = len(nums)
    cnt1 = cnt2 = 0
    el1 = el2 = None

    # Step 1: Find potential candidates
    for num in nums:
        if el1 == num:
            cnt1 += 1
        elif el2 == num:
            cnt2 += 1
        elif cnt1 == 0:
            el1 = num
            cnt1 = 1
        elif cnt2 == 0:
            el2 = num
            cnt2 = 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    # Step 2: Verify the candidates
    cnt1 = cnt2 = 0
    for num in nums:
        if num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1

    ans = []
    if cnt1 > n // 3:
        ans.append(el1)
    if cnt2 > n // 3:
        ans.append(el2)

    return ans


if __name__ == "__main__":
    arr = [1, 1, 1, 3, 3, 2, 2, 2]
    print("The majority elements are:", majorityElement(arr))
