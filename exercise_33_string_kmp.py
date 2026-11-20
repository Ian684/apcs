def solve(text, pattern):
    prefix = [0] * len(pattern)
    matched = 0
    for i in range(1, len(pattern)):
        while matched and pattern[i] != pattern[matched]: matched = prefix[matched - 1]
        if pattern[i] == pattern[matched]: matched += 1
        prefix[i] = matched
    matched = 0
    for i, char in enumerate(text):
        while matched and char != pattern[matched]: matched = prefix[matched - 1]
        if char == pattern[matched]: matched += 1
        if matched == len(pattern): return i - len(pattern) + 1
    return -1

if __name__ == "__main__":
    print("Exercise: 33_string_kmp")
