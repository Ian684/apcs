def solve(values):
    longest = current = 0
    previous = None
    for value in values:
        if value == previous:
            current += 1
        else:
            current = 1
            previous = value
        longest = max(longest, current)
    return longest

if __name__ == "__main__":
    print("Exercise: 15_longest_run")
