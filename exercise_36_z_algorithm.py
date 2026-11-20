def solve(text):
    combined = text
    z = [0] * len(combined)
    left = right = 0
    for i in range(1, len(combined)):
        if i <= right: z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < len(combined) and combined[z[i]] == combined[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right: left, right = i, i + z[i] - 1
    return z

if __name__ == "__main__":
    print("Exercise: 36_z_algorithm")
