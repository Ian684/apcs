def solve(n):
    if n < 2: return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

if __name__ == "__main__":
    print("Exercise: 16_climb_stairs")
