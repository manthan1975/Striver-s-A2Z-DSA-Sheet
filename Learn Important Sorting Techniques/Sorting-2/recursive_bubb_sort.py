def rec_bubb_sort(arr,n):
    if(n == 1):
        return
    
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
                
    rec_bubb_sort(arr,n-1)

def print_arr(arr,n):
    for i in range(n):
        print(arr[i],end=' ')
    print()

if __name__ == "__main__":
    arr = [4,1,2,3,5]
    n = len(arr)

    rec_bubb_sort(arr,n)
    print_arr(arr,n)