#brute force O(n^2)

def majority_element(arr):
    n = len(arr)
    i,j = 0,0

    for i in range(n):
        cnt =0
        for j in range(n):
            if arr[i]==arr[j]:
                cnt +=1

        if cnt> n//2:
            return arr[i]
        
#better
from collections import Counter
def majority_element1(arr):
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1


#Optimal O(n)
def majority_element2(arr):
    n = len(arr)
    cnt = 0
    el = None

    for i in range(n):
        if cnt==0:
            el = arr[i]
            cnt +=1
        elif el==arr[i]:
            cnt +=1
        else :
            cnt -=1

#check if selected element is majaority
    cnt1 =0
    for i in range(n):
        if arr[i]== el:
            cnt1 +=1

    if cnt1 > n//2:
        return el
    return -1





nums = [2,2,1,1,1,2,2]
output = majority_element(nums)

output1 = majority_element1(nums)
output2 = majority_element2(nums)
print(output)
print(output1)
print(output2)