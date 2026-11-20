def solve(prices):
    best = 0
    minimum = prices[0]
    for price in prices[1:]:
        minimum = min(minimum, price)
        best = max(best, price - minimum)
    return best

if __name__ == "__main__":
    print("Exercise: 02_stock_profit")
