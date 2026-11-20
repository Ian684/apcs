import collections
num = int(input())
for i in range(num):
    try:
        m , n = map(int , input().split())
        arr = []
        for o in range(m):
            ou = input()
            ou = ' '.join(ou).split()
            arr.append(ou)
        check = [[False]*n for _ in range(m)]
        result = []
        for x in range(m):
            for y in range(n):
                if check[x][y] == False:
                    queue = collections.deque([[x , y , arr[x][y]]])
                    result.append(arr[x][y])
                    while queue:
                        x_ , y_ , number= queue.popleft()
                        for dir_x , dir_y in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nx , ny = x_ + dir_x , y_ + dir_y
                            if 0 <= nx < m and 0 <= ny < n and check[nx][ny] == False and arr[nx][ny] == number:
                                check[nx][ny] = True
                                queue.append([nx , ny , arr[nx][ny]])
        result_plus = {}
        for c in result:
            if c not in result_plus:
                result_plus[c] = 1
            else:
                result_plus[c] = result_plus[c] + 1
        result_plus = dict(sorted(result_plus.items() , key = lambda item:(-item[1] ,item[0])))
        print(f'World #{i+1}')
        for key , value in result_plus.items():
            print(f'{key}: {value}')
    except:
        exit()