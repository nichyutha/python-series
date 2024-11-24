'''
Reverse the given array in place
'''
def reverseArray(arr):
    n = len(arr)

    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n-1-i]
        arr[n-i-1] = temp
    return arr

arr = [20,13,50,23,14,78,0,23]
result = reverseArray(arr)
print(result)

'''Complexity - Time : O(n) - Space: O(1)'''