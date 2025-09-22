# Time complexity = O(n)
# Space complexity = O(n)

def func(i,n):
    if(i>n):
        return
    print("Manthan")

    func(i+1,n)

func(1,n=4)

