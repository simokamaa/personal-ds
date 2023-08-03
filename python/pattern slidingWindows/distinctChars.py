#Given a string S, find the longest substring with K distinct characters

def longest_substring_with_k_distinct_chars(S, K):
    if K == 0:
        return 0

    char_freq = {}
    left, right = 0, 0
    max_length = 0

    while right < len(S):
        char_freq[S[right]] = char_freq.get(S[right], 0) + 1

        while len(char_freq) > K:
            char_freq[S[left]] -= 1
            if char_freq[S[left]] == 0:
                del char_freq[S[left]]
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length

# Example usage
S = "eceba"
K = 2
print(longest_substring_with_k_distinct_chars(S, K))  # Output: 3
