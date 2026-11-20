def solve(values):
    result = []
    def backtrack(index):
        if index == len(values): result.append(values[:]); return
        for i in range(index, len(values)):
            values[index], values[i] = values[i], values[index]
            backtrack(index + 1)
            values[index], values[i] = values[i], values[index]
    backtrack(0)
    return result

if __name__ == "__main__":
    print("Exercise: 39_permutation")
