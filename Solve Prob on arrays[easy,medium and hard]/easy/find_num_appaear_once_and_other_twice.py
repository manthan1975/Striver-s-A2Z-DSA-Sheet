# Optimal aproach
# Time complexity: O(n)
# Space complexity: O(1)

def get_single_elem(arr):
    xor = 0
    for num in arr:
        xor ^= num
    return xor


arr = [1,1,2,2,3,4,4]
print("The single elem is: ",get_single_elem(arr))