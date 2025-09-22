# Approach 1: Using a temp array 
#-> For Rotating the Elements to right

def rotate_right(arr,n,k):
    if(n == 0):
        return
    k = k % n

    if(k > n):
        return
    temp = [0] * k  

    for i in range(n-k,n):
        temp[i - n + k] = arr[i]
    
    for i in range(n-k-1,-1,-1):
        arr[i + k] = arr[i]

    for i in range(0,k):
        arr[i] = temp[i]

    
if __name__ == "__main__":
    n = 7
    arr = [1,2,3,4,5,6,7]
    k = 2
    rotate_right(arr,n,k)

    print("After rotating the elem to right: ")

    for i in range(0,n):
        print(arr[i],end=' ')
    print()
 



#-> For Rotating the Elements to left

def rotate_left(arr,n,k):
    if(n == 0):
        return
    k = k % n

    if(k > n):
        return
    temp = [0] * k  

    for i in range(0,k):
        temp[i] = arr[i]

    for i in range(0,n-k):
        arr[i] = arr[i + k]

    for i in range(n-k,n):
        arr[i] = temp[i - n + k]

    
if __name__ == "__main__":
    n = 7
    arr = [1,2,3,4,5,6,7]
    k = 2
    rotate_left(arr,n,k)

    print("After rotating the elem to left: ")

    for i in range(0,n):
        print(arr[i],end=' ')
    print()


# Approach 2: Using ” Reversal Algorithm “
# -> For Rotating Elements to right

def Reverse(arr,start,end):
    while(start <= end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -=1 


def rotate_right(arr,n,k):
  Reverse(arr, 0, n - k - 1)
  Reverse(arr, n - k, n - 1)
  Reverse(arr, 0, n - 1)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    n = 7
    k = 2

    rotate_right(arr,n,k)

    print("After rotating the elem to right: ")

    for i in range(0,n):
        print(arr[i],end=' ')
    print()




# -> For Rotating Elements to left

def Reverse(arr,start,end):
    while(start <= end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -=1 

def rotate_left(arr,n,k):
    Reverse(arr, 0, k - 1)
    Reverse(arr, k, n - 1)
    Reverse(arr, 0, n - 1)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    n = 7
    k = 2

    rotate_left(arr,n,k)

    print("After rotating the elem to left: ")

    for i in range(0,n):
        print(arr[i],end=' ')
    print()

