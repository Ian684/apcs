def solve(values, target):
    seen = {0: 1}
    prefix = 0
    answer = 0
    for value in values:
        prefix += value
        answer += seen.get(prefix - target, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return answer

if __name__ == "__main__":
    print("Exercise: 05_subarray_prefix")
