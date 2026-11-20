def solve(base, exponent, modulus):
    answer = 1
    base %= modulus
    while exponent:
        if exponent & 1: answer = answer * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return answer

if __name__ == "__main__":
    print("Exercise: 24_power_mod")
