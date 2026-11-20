def solve(text):
    best = ""
    for center in range(len(text)):
        for left, right in ((center, center), (center, center + 1)):
            while left >= 0 and right < len(text) and text[left] == text[right]:
                if right - left + 1 > len(best): best = text[left:right + 1]
                left -= 1; right += 1
    return best

if __name__ == "__main__":
    print("Exercise: 35_longest_palindrome")
