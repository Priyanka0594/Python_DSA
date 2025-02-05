#brute Force O(2n)
def sort_0_1_2(arr):
    n = len(arr)
    cnt0,cnt1,cnt2 = 0,0,0

    #count number of 0s,1s,2s
    for i in range(n):
        if arr[i]==0:
            cnt0 +=1
        
        elif arr[i]==1:
            cnt1 +=1
        
        elif arr[i]==2 :
            cnt2 += 1

    # put it in required order

    for i in range(cnt0):
        arr[i]=0
    
    for i in range(cnt0,cnt0+cnt1):
        arr[i]=1

    for i in range(cnt0+cnt1,n):
        arr[i]=2
    
    return arr

#optimal O(n)
def sort_0_1_2_opt(arr):
    n = len(arr)
    low,mid = 0,0
    high = n-1

    while mid<high:
        if arr[mid]==0:
            arr[low],arr[mid] = arr[mid],arr[low]
            mid +=1
            low +=1
        elif arr[mid]==1:
            mid +=1
        elif arr[mid]==2:
            arr[high],arr[mid]= arr[mid],arr[high]
            high -=1
    return arr
        


nums = [2,0,2,1,1,0]
output = sort_0_1_2(nums)
print(output)
    

output1 = sort_0_1_2_opt(nums)
print(output1)
