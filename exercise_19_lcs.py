def solve(left, right):
    dp = [[0] * (len(right) + 1) for _ in range(len(left) + 1)]
    for i in range(1, len(left) + 1):
        for j in range(1, len(right) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if left[i - 1] == right[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

if __name__ == "__main__":
    print("Exercise: 19_lcs")
