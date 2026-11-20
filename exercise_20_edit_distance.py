def solve(left, right):
    dp = list(range(len(right) + 1))
    for i, left_char in enumerate(left, 1):
        previous = dp.copy()
        dp[0] = i
        for j, right_char in enumerate(right, 1):
            dp[j] = previous[j - 1] if left_char == right_char else 1 + min(previous[j], dp[j - 1], previous[j - 1])
    return dp[-1]

if __name__ == "__main__":
    print("Exercise: 20_edit_distance")
