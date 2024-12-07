'''
Rotate the array to the left
by d timesm where d is any positive integer.
Do the change in place
'''

#approach - divide 'd' / reverse 

def rotateArray(arr,d):
    n = len(arr)

    d %= n # handles if d > size of array

    reverse(arr,0,d-1) # reverse d elements starting from 0
    reverse(arr,d,n-1) # reverse rest of elements from d
    reverse(arr,0,n-1) # reverse entire array


def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

arr = [10,20,30,40,50]
rotateArray(arr,12)
print(arr)

# Complexity - Time: O(n) Space: O(1)