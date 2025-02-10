import sys
def find_floor_ceil(arr,x):

    # Distances of current 
    # floor and ceiling 
    fDist = sys.maxsize 
    cDist = sys.maxsize 
    floor , ceil = -1,-1
    n = len(arr)
    
    for i in range(n): 
        
        # If current element is closer  
        # than previous ceiling. 
        if (arr[i] >= x and 
            cDist > (arr[i] - x)): 
            
            cInd = i 
            cDist = arr[i] - x 
    
        # If current element is closer  
        # than previous floor. 
        if (arr[i] <= x and fDist > (x - arr[i])): 
            
            fInd = i 
            fDist = x - arr[i] 
    
    if (fDist == sys.maxsize): 
        floor = -1
    else: 
        floor = arr[fInd]
    
    if (cDist == sys.maxsize): 
        ceil = -1
    else: 
        ceil = arr[cInd]
        
    return floor,ceil

x = 7 
arr = [5, 6, 8, 9, 6, 5, 5, 6]

output =  find_floor_ceil(arr,x)
print(output)
    