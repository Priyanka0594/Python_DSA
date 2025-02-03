def array_union(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr = []
    i,j = 0,0

    while i< n1 and j<n2:
        if arr1[i]<arr2[j] :
            if arr1[i] not in arr:
                arr.append(arr1[i])
            i+=1

        elif arr2[j]>arr1[i] :
            if arr[j] not in arr:
                arr.append(arr2[j])
            j+=1
        
        else:
            if arr1[i] not in arr:
                arr.append(arr1[i])
            i+=1
            j+=1
    
    while i<n1 :
        if arr1[i] not in arr:
            arr.append(arr1[i])
        i+=1
    
    while j<n2 :
        if arr2[j] not in arr:
            arr.append(arr2[j])
        j+=1
        
    return arr

#example
output = array_union([1,2,3,4,5],[1,4,5,8])
print(output)
    