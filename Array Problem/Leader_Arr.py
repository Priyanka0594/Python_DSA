#brute force O(n^2)

def leader_arr(arr):
    n = len(arr)
    list = []
    

    for i in range(n-1):
        chk = 0
        for j in range(i+1,n):
            if arr[i]< arr[j]:
                chk = 1
                break
        
        if chk == 0:
            list.append(arr[i])
    list.append(arr[n-1])
    
    return list


#optimal
def leader_arr1(arr):
    n = len(arr)
    ans=[]
    max = arr[n-1]
    ans.append(arr[n-1])

    for i in range (n-2,-1,-1):
        if arr[i]>max:
            ans.append(arr[i])
            max = arr[i]
    
    ans1 =[]
    for i in range(len(ans)-1,-1,-1):
        ans1.append(ans[i])

    return ans1


arr = [4, 7, 1, 0]

output = leader_arr(arr)

output1 = leader_arr1(arr)
print(output)
print(output1)


