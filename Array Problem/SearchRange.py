def searchRange( nums, target):
    first = -1
    last = -1
    n = len(nums)

    for i in range(n):
        if nums[i]== target:
            first = i
            break
    
    for i in range(n-1,-1,-1):
        if nums[i]==target:
            last = i
            break
    
    return [first,last]

def countFreq( arr, target):
    #code here
    first = -1
    last = -1
    n = len(arr)

    for i in range(n):
        if arr[i]== target:
            first = i
            break
    
    for i in range(n-1,-1,-1):
        if arr[i]==target:
            last = i
            break
    
    if last == first and last== -1:
        return 0 
    elif last == first and last != -1:
        return 1
    else:
        return last-first+1

nums = [5,7,7,8,8,10]
target = 8

output = searchRange(nums,target)
output1= countFreq(nums,target)
print(output)
print(output1)