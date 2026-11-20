def solve(intervals):
    intervals.sort()
    merged = []
    for left, right in intervals:
        if not merged or left > merged[-1][1]:
            merged.append([left, right])
        else:
            merged[-1][1] = max(merged[-1][1], right)
    return merged

if __name__ == "__main__":
    print("Exercise: 03_interval_merge")
