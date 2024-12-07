'''
Given an array, find the frequency of number if it is repated more than n/3 time.
'''

#approch - moore's algo

def findFrequency(arr):
    n = len(arr)

    ele1, ele2 = -1,-1
    cnt1,cnt2 = 0,0

    for ele in arr:
        if ele1 == ele:
            cnt1 +=1
        elif ele2 == ele:
            cnt2 +=1
        elif cnt1 == 0:
            ele1 = ele
            cnt1 +=1
        elif cnt2 ==0:
            ele2 = ele
            cnt2 += 1
        #decrement count if neither of elements match
        else:
            cnt1 -=1
            cnt2 -=1
    res = []
    cnt1,cnt2 =0,0

    for ele in arr:
        if ele1 == ele:
            cnt1 +=1
        if ele2 == ele:
            cnt2 +=1
        
    if cnt1 > n/3 :
        res.append(ele1)
    if cnt2 > n/3 and ele1 != ele2:
        res.append(ele2)
    # rearrange result in acending order
    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res

arr = [2,1,1,1,4,1,2,2]
result = findFrequency(arr) 
print(result)

# complexity - Time:O(n) space: O(1)