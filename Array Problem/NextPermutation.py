def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    ind = -1
    #find the place from back where there was decrement in number 

    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            ind = i
            break 
    
    # if no such decrement found means its max number and return reverse 
    if ind == -1:
        return nums.reverse()

    # from back swap the ind with number closest and bigger than index
    for i in range (n-1,ind,-1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind] , nums[i]
            break

    #reverse the remaining array
    nums[ind+1:] = reversed(nums[ind+1:])
    
    return nums

#example 

nums = [2,1,3]

output = nextPermutation(nums)
print(output)