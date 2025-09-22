def changearr(arr,size):
    print("In Func: ")
    for i in range(0,size):
        arr[i] = 2 * arr[i]


if __name__ == "__main__":
    arr = [1,2,3] 

    changearr(arr,3)

    print("In main: ")
    for i in range(0,3):
        print(arr[i])


