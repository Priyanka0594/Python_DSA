def bubblesort(arr):
    n = len(arr)
    for i in range(n,0,-1):
        for j in range(0,i-1,1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr


# Example usage
arr = [1,2,3,4,9,2,1]
output = bubblesort(arr)
print("Output:", output)