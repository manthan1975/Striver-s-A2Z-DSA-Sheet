def rev_arr(arr,size):
    start = 0 
    end = size - 1

    while(start < end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1 



if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    size = len(arr)

    rev_arr(arr,size)

    for i in range(0,size):
        print(arr[i],end=' ')