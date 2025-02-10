#Brute Force O(n^2)
def maxProfit(arr):
    n = len(arr)
    maxpro = 0

    for i in range(n):
        for j in range(i+1,n):
            maxpro= max(arr[j]-arr[i],maxpro)

    return maxpro




#Optimal O(n)
def maxProfit1(arr):
    n = len(arr)
    mini = float('inf')
    profit = 0

    for i in range(1,n):
        mini = min(arr[i],mini)
        profit = max(profit,arr[i] - mini)

    return profit

arr = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(arr)

maxPro1 = maxProfit1(arr)
print(maxPro1, maxPro)