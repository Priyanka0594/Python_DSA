import sys
#brute Force O(n^2)
def maxsubarray(arr):
    n = len(arr)
    maxsum = -sys.maxsize - 1
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]

            if sum > maxsum:
                maxsum = sum
   
    return maxsum


#Optimal O(n)
def maxsubarray1(arr):
    n = len(arr)
    sum = 0
    ansarr = []
    ansstart,ansend = 0,0
    maxsum = - (sys.maxsize - 1)
    for i in range(n):
        if sum == 0 :
            start = i

        sum += arr[i]

        if sum > maxsum:
            maxsum= sum
            ansstart = start
            ansend = i

        if sum < 0:
            sum = 0
    
    print(maxsum)
    for i in range(ansstart,ansend+1):
        ansarr.append(arr[i])
    print(ansarr)



arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
output = maxsubarray(arr)
maxsubarray1(arr)
print(output)