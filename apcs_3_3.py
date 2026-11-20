import collections
def go(arr , n , target , l , r):
    queue = collections.deque([[0 , 0]])
    check = [False]*n
    while queue:
        current , step = queue.popleft()
        if current == target:
            return step
        for i in [-l , r]:
            pcurrent = current + i
            if 0 <= pcurrent < n and check[pcurrent] != True:
                if arr[pcurrent] < n and arr[pcurrent] >= 0:
                    check[pcurrent] = True
                    queue.append([arr[pcurrent] , step + 1])
    return -1
if __name__ == '__main__':
    n , target , l , r = map(int , input().split())
    arr = list(map(int , input().split()))
    print(go(arr , n , target , l , r))