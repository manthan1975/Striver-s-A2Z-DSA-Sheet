# Ascending Order
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
        


def merge_sort(arr,st,end):
    if(st < end):
        mid = st + (end-st)//2

        merge_sort(arr,st,mid)        # Left Half
        merge_sort(arr,mid+1,end)     # Right Half

        merge(arr,st,mid,end)


if __name__ == "__main__":
    arr = [12,31,35,8,17,32]

    merge_sort(arr,0,len(arr) - 1)

    for val in arr:
        print(val, end=" ")
    print()






# Descending Order

def merge(arr,st,mid,end):
    temp = []
    i = st 
    j = mid + 1

    while(i <= mid and j <= end):
        if(arr[i] >= arr[j]):
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
        


def merge_sort(arr,st,end):
    if(st < end):
        mid = st + (end-st)//2

        merge_sort(arr,st,mid)        # Left Half
        merge_sort(arr,mid+1,end)     # Right Half

        merge(arr,st,mid,end)


if __name__ == "__main__":
    arr = [12,31,35,8,17,32]

    merge_sort(arr,0,len(arr) - 1)

    for val in arr:
        print(val, end=" ")
    print()
