# Time Complexity: O(n)  
# Space Complexity: O(1)

def linear_search(arr,size):
    for i in range(0,size):
        if(arr[i] == target):     #FOUND
            return i
        
    
    return -1             # NOT FOUND


if __name__ == "__main__":
    arr = [4,2,7,8,1,2,5]
    size = len(arr)
    target = 5

    print(linear_search(arr,size,))
