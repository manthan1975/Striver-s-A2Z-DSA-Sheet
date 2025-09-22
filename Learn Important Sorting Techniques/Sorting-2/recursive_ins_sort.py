def rec_ins_sort(arr,i,n):
    if i==n:
        return
    j = i
    while(j >= 0 and arr[j-1] > arr[j]):
           arr[j],arr[j-1] = arr[j-1],arr[j]
        
    rec_ins_sort(arr, i + 1, n)



def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


if __name__ == "__main__":
    arr = [4, 1, 2, 3, 5]
    n = len(arr)

    rec_ins_sort(arr,1,n)
    print_arr(arr, n)