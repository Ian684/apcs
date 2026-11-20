def solve(n):
    def multiply(a, b):
        return ((a[0]*b[0]+a[1]*b[2]), (a[0]*b[1]+a[1]*b[3]), (a[2]*b[0]+a[3]*b[2]), (a[2]*b[1]+a[3]*b[3]))
    result = (1, 0, 0, 1)
    base = (1, 1, 1, 0)
    while n:
        if n & 1: result = multiply(result, base)
        base = multiply(base, base)
        n >>= 1
    return result[1]

if __name__ == "__main__":
    print("Exercise: 21_fibonacci_fast")
