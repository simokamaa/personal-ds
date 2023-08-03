#finding maximum subarray of a given fixed size k
def max_sum_subarray(arr, k):
    n = len(arr)
    if k > n:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum + arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9 (Subarray: [5, 1, 3])
