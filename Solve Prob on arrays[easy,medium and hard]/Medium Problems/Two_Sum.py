# Bruteforce approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def findTwo_sum(arr,n,tar,):
    ans = []
    for i in range(0,n):
        first = arr[i]
        for j in range(i+1,n):
            second = arr[j]
            sum = first + second
            if(sum == tar):
                ans.append(i)
                ans.append(j)
                return ans
    
    return -1

if __name__ == "__main__":
    arr = [5,2,11,7,15]
    n = len(arr)
    tar = 9
    print(findTwo_sum(arr,n,tar))


# Better approach
# Time Complexity: O(nLogn)
# Space Complexity: O(1)

def findTwo_sum(arr, tar):
    a = sorted(arr)
    st, end = 0, len(a) - 1
    while st < end:
        s = a[st] + a[end]
        if s == tar:
            return [a[st], a[end]]
        elif s < tar:
            st += 1
        else:
            end -= 1
    return -1

if __name__ == "__main__":
    arr = [5,2,11,7,15]
    tar = 9
    print(findTwo_sum(arr,tar))


# Optimized approach
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, arr, tar):
        m = {}   # dictionary works as hashmap
        ans = []

        for i in range(len(arr)):
            first = arr[i]
            sec = tar - first

            if sec in m:
                ans.append(i)
                ans.append(m[sec])
                break
            m[first] = i
    
        return ans