#given a string S and string T.Find minimum window in S that contain
#all characters in T

# S = "ADOBECODEBANC"
# T = "ABC"

def min_window_substring(S, T):
    from collections import Counter

    t_counts = Counter(T)
    required_chars = len(t_counts)
    formed_chars = 0
    left, right = 0, 0
    min_window_size = float('inf')
    min_window = ""

    while right < len(S):
        if S[right] in t_counts:
            t_counts[S[right]] -= 1
            if t_counts[S[right]] == 0:
                formed_chars += 1

        while formed_chars == required_chars and left <= right:
            if right - left + 1 < min_window_size:
                min_window_size = right - left + 1
                min_window = S[left:right + 1]

            if S[left] in t_counts:
                t_counts[S[left]] += 1
                if t_counts[S[left]] > 0:
                    formed_chars -= 1

            left += 1

        right += 1

    return min_window

# Example usage
S = "ADOBECODEBANC"
T = "ABC"
print(min_window_substring(S, T))  # Output: "BANC"

