def xp(m, n, arr):
    result_c = float('-inf')
    visited = [[False]*n for _ in range(m)]
    def dfs(x, y, count):
        nonlocal result_c
        if x == m-1:
            if count > result_c:
                result_c = count
        for dx, dy in [(1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, count + arr[nx][ny])
                visited[nx][ny] = False
    for j in range(n):
        visited[0][j] = True
        dfs(0, j, arr[0][j])
        visited[0][j] = False
    return result_c
if __name__ == '__main__':
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    print(xp(m, n, arr))
# 上下左右for
# 紀錄步伐[[False]*i for i in range()]
# nonlocal float('-inf')
