def solve(limit):
    prime = [True] * (limit + 1)
    prime[0:2] = [False, False]
    for value in range(2, int(limit ** 0.5) + 1):
        if prime[value]:
            for multiple in range(value * value, limit + 1, value): prime[multiple] = False
    return [value for value, is_prime in enumerate(prime) if is_prime]

if __name__ == "__main__":
    print("Exercise: 23_sieve_prime")
