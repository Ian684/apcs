def xp(m ,n ,arr):
    result_c = -99999
    def calculate(a ,b ,arr ,count):
        nonlocal result_c
        if a-1>=0:
            if arr[a-1][b] != '.':
                t = arr[a-1][b]
                arr[a-1][b] = '.'
                calculate(a-1 ,b ,arr,count+t)
                arr[a-1][b] = t
        if a+1<m:
            if arr[a+1][b] != '.':
                t = arr[a+1][b]
                arr[a+1][b] = '.'
                calculate(a+1 ,b ,arr,count+t)
                arr[a+1][b] = t
        if b-1>=0:
            if arr[a][b-1] != '.':
                t = arr[a][b-1]
                arr[a][b-1] = '.'
                calculate(a ,b-1 ,arr,count+t)
                arr[a][b-1] = t
        if b+1<n:
            if arr[a][b+1] != '.':
                t = arr[a][b+1]
                arr[a][b+1] = '.'
                calculate(a ,b+1 ,arr,count+t)
                arr[a][b+1] = t
        if count > result_c:
            result_c = count
        if (a-1<0 or arr[a-1][b]=='.')and(a+1>=m or arr[a+1][b]=='.')and(b-1<0 or arr[a][b-1]=='.')and(b+1>=n or arr[a][b+1]=='.'):
            return
    for i in range(n):
        t = arr[0][i]
        arr[0][i] = '.'
        calculate(0 ,i ,arr ,t)
        arr[0][i] = t
    return result_c
if __name__ == '__main__':
    m ,n = map(int ,input().split())
    arr = []
    for i in range(m):
        arr.append(list(map(int ,input().split())))
    print(xp(m ,n ,arr))