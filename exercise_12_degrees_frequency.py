def solve(values):
    frequencies = {}
    for value in values:
        frequencies[value] = frequencies.get(value, 0) + 1
    return max(frequencies, key=lambda value: (frequences[value], value))

if __name__ == "__main__":
    print("Exercise: 12_degrees_frequency")
