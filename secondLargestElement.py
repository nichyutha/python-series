''' find second largest distinct number from an array
rule 1: if no second largest number exist return -1
'''


def find2Largest(arr):
    n = len(arr)
    if n < 2:
        return -1
    
    first = second = float('-inf')
    
    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    
    if second == float('-inf'):
        return -1
    else:
        return second


arr = [3,20,12,45,37,10,8]
result = find2Largest(arr)
print(result)

'''Time complexity O(n) Space complexicty O(1)'''