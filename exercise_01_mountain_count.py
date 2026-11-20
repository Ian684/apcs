def solve(values):
    count = 0
    for i in range(1, len(values) - 1):
        if values[i] > values[i - 1] and values[i] > values[i + 1]:
            count += 1
    return count

if __name__ == "__main__":
    print("Exercise: 01_mountain_count")
