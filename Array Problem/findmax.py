def findmax(arr):
    max = arr[0]
    n = len(arr)

    #iterate over array 
    for i in range(1,n):
        if arr[i]>max:
            max= arr[i]
    
    return max

findmax([1,2,36,4,5])
