import copy

n, m, k = map(int, input().split())
list_Q = [list(map(int, input().split())) for _ in range(n)]
list_C = [list(map(int, input().split())) for _ in range(k)]
ans = []
for c in range(k):  # 每次看一个方案
    money = 0
    temp_q = copy.deepcopy(list_Q)
    temp_c = copy.deepcopy(list_C[c])
    i = 0
    while i < len(temp_c):  # 不能使用for迴圈 必須改用while代替
        j = i + 1
        while j < len(temp_c):
            if temp_c[i] == temp_c[j]:
                for m in range(len(temp_q[i])):
                    temp_q[i][m] += temp_q[j][m]  # 相同的地區流量合併
                temp_q.pop(j)
                temp_c.pop(j)
            else:
                j += 1
        i += 1

    for i in range(len(temp_q)):
        for j in range(len(temp_q[i])):
            if temp_c[i] == j:
                money += temp_q[i][j]
            elif temp_q[i][j] > 1000:
                money += (temp_q[i][j] - 1000) * 2 + 3000
            else:
                money += temp_q[i][j] * 3
    ans.append(money)

print(min(ans))
