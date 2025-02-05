#Brute Force O(n^2)

def find_pairs_with_sum1(arr, target_sum):
    n = len(arr)
    pairs = []
    i,j = 0,0
    for i in range(n):
        for j in range(i+1,n):
            sum = arr[i] + arr[j]
            if sum == target_sum:
                pairs.append([i,j])

    
    return pairs


# optimal O(n)
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    arr.sort()  # Ensure the array is sorted
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            pairs.append((left, right))
            left += 1
            right -= 1  # Move both pointers inward
        elif current_sum < target_sum:
            left += 1  # Increase the left pointer
        else:
            right -= 1  # Decrease the right pointer
    
    return pairs

# Example usage
arr = [1, 3, 4, 5, 7, 8, 9, 10]
target_sum = 10
result = find_pairs_with_sum(arr, target_sum)
print("Pairs with sum 10:", result)

result = find_pairs_with_sum1(arr, target_sum)
print("Pairs with sum 10:", result)