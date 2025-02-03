def search(arr, s):
    n = len(arr)

    for i in range(n):
        if arr[i] == s:
            return i
        
#example
nums =[1, 2, 3, 4, 5]
print(search(nums,2))