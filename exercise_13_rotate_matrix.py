def solve(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

if __name__ == "__main__":
    print("Exercise: 13_rotate_matrix")
