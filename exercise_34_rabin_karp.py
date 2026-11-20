def solve(text, pattern):
    base, modulus = 256, 1_000_000_007
    if len(pattern) > len(text): return -1
    text_hash = pattern_hash = 0
    power = 1
    for i in range(len(pattern) - 1): power = power * base % modulus
    for i in range(len(pattern)):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % modulus
        text_hash = (base * text_hash + ord(text[i])) % modulus
    for i in range(len(text) - len(pattern) + 1):
        if text_hash == pattern_hash and text[i:i + len(pattern)] == pattern: return i
        if i < len(text) - len(pattern): text_hash = (base * (text_hash - ord(text[i]) * power) + ord(text[i + len(pattern)])) % modulus
    return -1

if __name__ == "__main__":
    print("Exercise: 34_rabin_karp")
