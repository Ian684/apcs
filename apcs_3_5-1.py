from collections import defaultdict
p , q , r , m = map(int , input().split())
ip=list(map(int,input().split()))
gate=list(map(int,input().split()))
graph=defaultdict(list)
for i in range(m):
    a , b = map(int , input().split())
    graph[b].append(a)
delay = [0]*(p+q)
value = [-1]*(p+q+r)

def dfs(x):
    if value[x-1] != -1:return
    if x <= p:
        value[x-1] = ip[x-1]
        return
    elif p < x <= p+q:
        if 1 <= gate[x-p-1] <= 3:
            dfs(graph[x][0])
            dfs(graph[x][1])
            value[x-1] = calculate(value[graph[x][0]-1],value[graph[x][1]-1],gate[x-p-1])
            delay[x-1] = max(delay[graph[x][0]-1],delay[graph[x][1]-1])+1
        else:
            dfs(graph[x][0])
            value[x-1] = int(not value[graph[x][0]-1])
            delay[x-1]=delay[graph[x][0]-1]+1
    else:
        dfs(graph[x][0])
        value[x-1] = value[graph[x][0]-1]
def calculate(g1 , g2 , g3):
    if g3==1:
        return g1 and g2
    elif g3==2:
        return g1 or g2
    else:
        return g1^g2
for i in range(p+q,p+q+r+1):
    dfs(i)
print(max(delay))
print(' '.join(list(map(str , value[p+q:p+q+r:]))))
