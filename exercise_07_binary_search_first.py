def solve(values, target):
    left, right = 0, len(values)
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left if left < len(values) and values[left] == target else -1

if __name__ == "__main__":
    print("Exercise: 07_binary_search_first")
