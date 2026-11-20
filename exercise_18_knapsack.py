def solve(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            dp[current] = max(dp[current], dp[current - weight] + value)
    return dp[capacity]

if __name__ == "__main__":
    print("Exercise: 18_knapsack")
