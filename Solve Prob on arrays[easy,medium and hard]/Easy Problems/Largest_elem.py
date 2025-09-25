# 1st method
def findLargest(arr):
    if not arr:  
        return None
    
    largest = float("-inf")
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

if __name__ == "__main__":
    arr = [12,14,17,34,45,56,78]
    print(findLargest(arr))




    
# 2nd method

# num = [12, 14, 56, 23, 43, 78, 1000]

# largest = max(num)   
# print("The largest element in the array is:", largest)

