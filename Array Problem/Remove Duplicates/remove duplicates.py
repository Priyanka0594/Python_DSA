def rmvdup(nums):
    if not nums:
        return 0  # If the array is empty, return 0

    # Initialize the write pointer
    write_index = 1

    # Iterate through the array with the read pointer
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    # Return the length of the array with unique elements
    return write_index
                    
            
arr = [1,2,3,3,4,5,6,6,7]
output = rmvdup(arr)
print("Output:", output)