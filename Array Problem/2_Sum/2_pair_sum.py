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