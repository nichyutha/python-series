'''
Given array represents Permutation, implement Next combination of permutation
that rearrages the numbers into lexicographically with next combination.
'''

def next_permutation(arr):
    n = len(arr)

    pivot = -1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            pivot = i
            break

    if pivot == -1:
        arr.reverse()
        return

    # find element greater than pivot
    for i in range(n-1,pivot,-1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break
    
    # reverse the elements from pivot+1 till end
    left, right = pivot+1, n-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1

arr = [3,6,1,2,8,7]
next_permutation(arr)
print(arr)
