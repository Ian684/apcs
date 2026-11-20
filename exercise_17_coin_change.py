def solve(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for value in range(1, amount + 1):
        dp[value] = min(dp[value - coin] + 1 for coin in coins if coin <= value)
    return dp[amount] if dp[amount] <= amount else -1

if __name__ == "__main__":
    print("Exercise: 17_coin_change")
