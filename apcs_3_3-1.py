import collections
def maze():
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                start_x , start_y = i , j
    queue = collections.deque([(start_x , start_y , 0)])
    check[start_x][start_y] = True
    while queue:
        x , y , step = queue.popleft()
        if arr[x][y] == 2:
            return step
        for dir_x , dir_y in [(-1,0) , (1,0) , (0,-1) , (0,1)]:
            nx , ny = dir_x + x , dir_y + y
            if 0 <= nx < m and 0 <= ny < n:
                if check[nx][ny] == False and arr[nx][ny] != -1:
                    check[nx][ny] = True
                    queue.append((nx , ny , step+1))
if __name__ == '__main__':
    m , n = map(int , input().split())
    arr = [list(map(int , input().split())) for _ in range(m)]
    check = [[False]*n for _ in range(m)]
    print(maze())