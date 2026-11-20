def solve(n):
    result = []
    columns, diagonal_one, diagonal_two = set(), set(), set()
    board = [-1] * n
    def backtrack(row):
        if row == n:
            result.append(board[:]); return
        for column in range(n):
            if column in columns or row-column in diagonal_one or row+column in diagonal_two: continue
            columns.add(column); diagonal_one.add(row-column); diagonal_two.add(row+column); board[row] = column
            backtrack(row+1)
            columns.remove(column); diagonal_one.remove(row-column); diagonal_two.remove(row+column)
    backtrack(0)
    return result

if __name__ == "__main__":
    print("Exercise: 40_n_queens")
