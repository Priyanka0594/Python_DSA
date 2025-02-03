def longest_subArray_for_sumk(arr,k):
    n = len(arr)
    sum = 0
    length = 0

    for i in range(n):
        for j in range(i,n,1):
            sum += arr[j]
            if sum == k:
                length = max(length,j-i+1)
    
    return length


#example
a = [2, 3, 5, 1, 9]
k = 10
output = longest_subArray_for_sumk(a,k)
print(output)