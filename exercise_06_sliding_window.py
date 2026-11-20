def solve(values, limit):
    left = total = answer = 0
    for right, value in enumerate(values):
        total += value
        while total > limit:
            total -= values[left]
            left += 1
        answer = max(answer, right - left + 1)
    return answer

if __name__ == "__main__":
    print("Exercise: 06_sliding_window")
