def solve(values, target):
    seen = {}
    for index, value in enumerate(values):
        if target - value in seen:
            return [seen[target - value], index]
        seen[value] = index
    return []

if __name__ == "__main__":
    print("Exercise: 04_two_sum")
