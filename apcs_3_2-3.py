def test(arr):
    right = arr[0][:]
    dp = []
    for j in range(1 ,n):
        right[j] = max(right[j] ,right[j-1]+arr[0][j])
    left = arr[0][:]
    for j in range(n-2 ,-1 ,-1):
        left[j] = max(left[j] ,left[j+1]+arr[0][j])
    for i in range(n):
        dp.append(max(right[i] ,left[i]))
    for i in range(1 ,m):
        for j in range(n):
            right[j] = dp[j] + arr[i][j]
            left[j] = dp[j] + arr[i][j]
        for j in range(1 ,n):
            right[j] = max(right[j] ,right[j-1]+arr[i][j])
        for j in range(n-2 ,-1 ,-1):
            left[j] = max(left[j] ,left[j+1]+arr[i][j])
        for j in range(n):
            dp[j] = max(right[j] ,left[j])
    return max(dp)
if __name__ == '__main__':
    m ,n = map(int ,input().split())
    arr = []
    for i in range(m):
        arr.append(list(map(int ,input().split())))
    print(test(arr))
# dp 淺拷貝
