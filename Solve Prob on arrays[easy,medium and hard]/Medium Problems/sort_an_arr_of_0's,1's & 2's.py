# Brutefroce approach
# Time Complexity: O(nLogn)
# Space Complexity: O(1)

def merge(arr,st,mid,end):
    temp = []
    i = st 
    j = mid + 1

    while(i <= mid and j <= end):
        if(arr[i] <= arr[j]):
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while(i <= mid):
        temp.append(arr[i])
        i += 1

    while(j <= end):
        temp.append(arr[j])
        j += 1

    for idx in range(len(temp)):
        arr[idx + st] = temp[idx]
        


def sort(arr,st,end):
    if(st < end):
        mid = st + (end-st)//2

        sort(arr,st,mid)        # Left Half
        sort(arr,mid+1,end)     # Right Half

        merge(arr,st,mid,end)


if __name__ == "__main__":
    arr = [2,0,2,1,1,0]

    sort(arr,0,len(arr) - 1)

    for val in arr:
        print(val, end=" ")
    print()


# Better approach (It takes 2 pass)
# Time Complexity: O(n)
# Space Complexity: O(1)

def sort(arr):
    n = len(arr)
    count0 = 0
    count1 = 0
    count2 = 0

    for i in range(0,n):
        if(arr[i] == 0):
            count0 += 1
        elif(arr[i] == 1):
            count1 += 1
        else:
            count2 += 1

    
    idx = 0
    for i in range(0,count0):
        arr[idx] = 0
        idx += 1

    for i in range(0,count1):
        arr[idx] = 1
        idx += 1

    for i in range(0,count2):
        arr[idx] = 2
        idx += 1

    return arr

if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    print(sort(arr))


# Optimal approach (In a single pass Using DNF) 
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        low,mid,high = 0,0,n-1

        while(mid <= high):
            if(nums[mid] == 0):
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1

            elif(nums[mid] == 1):
                mid += 1

            else:
                nums[high],nums[mid] = nums[mid],nums[high]
                high -= 1