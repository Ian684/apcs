import collections
def jump_maze(arr):
    queue = collections.deque([(start_x , start_y , 0)])
    check = [[False]*n for _ in range(m)]
    check[start_x][start_y] = True
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                check[i][j] == True
    while queue:
        x , y , step= queue.popleft()
        if x == end_x and y == end_y:
            return step
        for dir_x , dir_y in [(0,-k) , (0,k)]:
            ny = y + dir_y
            if 0 <= ny < n:
                for i in range(min(y , ny) , max(y , ny)):
                    if check[x][i] == True:valid = False
                if arr[x][ny] != 1 and valid:
                    for i in range(min(y,ny) , max(y,ny)):
                        check[x][i] = True
                    queue.append((x , ny , step+1))          
        for dir_x , dir_y in [(-k,0) , (k,0)]:
            nx = x + dir_x
            valid = True
            if 0 <= nx < m:
                for i in range(min(x , nx) , max(x , nx)):
                    if check[i][y] == True:valid = False
                if arr[nx][y] != 1 and valid:
                    for i in range(min(x , nx) , max(x , nx)):
                        check[i][y] = True
                    queue.append((nx , y , step+1))     
    return -1
if __name__ == "__main__":
    m , n , k = map(int , input().split())
    arr = [list(map(int , input().split())) for _ in range(m)]
    start_x , start_y = map(int , input().split())
    end_x , end_y = map(int , input().split())
    print(jump_maze(arr))