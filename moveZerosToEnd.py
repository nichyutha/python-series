'''
Move all zeros to the end of an array
rule 1: Maintain relative order of all elements
rule 2: Do changes in place 
'''

def moveZerosToEnd(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0 :
            arr[i],arr[count] = arr[count], arr[i]
            count += 1

    return arr

arr = [1,2,6,9,0,11,45,0,0,32]
result = moveZerosToEnd(arr)
print(result)

'''Time Complexity : O(n) Space Complexity: O(1)'''