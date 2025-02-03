def selectionsort(arr):
    n = len(arr)
    

    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
                arr[i],arr[mini] = arr[mini],arr[i]

    return arr

# Example usage
arr = [1,2,3,4,9,2,1]
output = selectionsort(arr)
print("Output:", output)
    
