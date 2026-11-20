def solve(rows, columns):
    matrix = [[0] * columns for _ in range(rows)]
    top, bottom, left, right = 0, rows - 1, 0, columns - 1
    value = 1
    while top <= bottom and left <= right:
        for column in range(left, right + 1): matrix[top][column] = value; value += 1
        top += 1
        for row in range(top, bottom + 1): matrix[row][right] = value; value += 1
        right -= 1
        if top <= bottom:
            for column in range(right, left - 1, -1): matrix[bottom][column] = value; value += 1
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1): matrix[row][left] = value; value += 1
            left += 1
    return matrix

if __name__ == "__main__":
    print("Exercise: 14_spiral_matrix")
