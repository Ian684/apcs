def solve(values):
    seen = set()
    return [value for value in values if not (value in seen or seen.add(value))]

if __name__ == "__main__":
    print("Exercise: 08_deduplicate_preserve")
