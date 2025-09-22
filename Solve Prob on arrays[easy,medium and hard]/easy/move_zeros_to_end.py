def moveZero(nums):
    if not nums:
        return 0
    k = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1

    for i in range(k, len(nums)):
        nums[i] = 0
        
    return k


if __name__ == "__main__":
    arr = [1,0,2,3,0,4,0,1]
    k = moveZero(arr)
    print("Modified array: ",arr)