def leftrotatearr(arr,k):
    temp =[]
    n= len(arr)
    j=0

    for i in range(k):
        temp.append(arr[i])

    for i in range(k,n):
        arr[i-k] = arr[i]


    for i in range(n-k,n):
        arr[i]=temp[j]
        j +=1

    return arr

#example
nums = [1, 2, 3, 4, 5]
print(leftrotatearr(nums,2))