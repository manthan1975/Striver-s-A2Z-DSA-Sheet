# Ascending Order
def partition(arr,st,end):
    idx = st - 1
    pivot = arr[end]

    for j in range(st,end):
        if arr[j] <= pivot:
            idx += 1
            arr[j],arr[idx] = arr[idx],arr[j]

    idx += 1
    arr[end],arr[idx] = arr[idx],arr[end]
    return idx

def quick_sort(arr,st,end):
    if(st < end):
        pivIdx = partition(arr,st,end)

        quick_sort(arr,st,pivIdx-1)        # Left Half
        quick_sort(arr,pivIdx+1,end)       # Right Half

if __name__ == "__main__":
    arr = [12,31,35,8,17,32]
    quick_sort(arr,0,len(arr) - 1)

    for value in arr:
        print(value,end=' ')
    print()









# Descending Order

def partition(arr,st,end):
    idx = st - 1
    pivot = arr[end]

    for j in range(st,end):
        if arr[j] >= pivot:
            idx += 1
            arr[j],arr[idx] = arr[idx],arr[j]

    idx += 1
    arr[end],arr[idx] = arr[idx],arr[end]
    return idx

def quick_sort(arr,st,end):
    if(st < end):
        pivIdx = partition(arr,st,end)

        quick_sort(arr,st,pivIdx-1)        # Left Half
        quick_sort(arr,pivIdx+1,end)       # Right Half

if __name__ == "__main__":
    arr = [12,31,35,8,17,32]
    quick_sort(arr,0,len(arr) - 1)

    for value in arr:
        print(value,end=' ')
    print()
