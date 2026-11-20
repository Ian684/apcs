# if __name__ == "__main__":
#     try:
#         n , d = map(int , input().split())
#         arr = list(map(int , input().split()))
#         current = True
#         count = arr[0]
#         result = 0
#         for i in arr:
#             if i >= count+d and current == True:
#                 current = False
#                 result += i - count
#                 count = i
#             elif current == False and i <= count-d:
#                 current = True
#                 count = i
#         print(result)
#     except:
#         exit()


if __name__ == "__main__":
    from collections import defaultdict
    n , m = map(int , input().split())
    crr = []
    for i in range(3):
        crr.append(list(map(int , input().split())))
    l = len(crr[2])
    for i in range(l):
        crr[2][i] -= 1
    arr = defaultdict(list)
    for i in range(l):
        arr[crr[2][i]] = [crr[0][i] , crr[1][i] , 0]
    while True:
        victory = defaultdict(list)
        defeat = defaultdict(list)
        if len(arr) == 1:
            break
        for i in range(0 , len(arr) , 2):
            a , b , c , d = arr[i][0] , arr[i][1] , arr[i+1][0] , arr[i+1][1]
            if a*b >= c*d:
                victory[i] = [a+c*d//(2*b) , b+c*d//(2*a) , arr[i][2]]
                if arr[i+1][2] < m :defeat[i+1] = [c+c//2 , d+d//2 , arr[i+1][2]+1]
            elif a*b < c*d:
                if arr[i][2] < m :defeat[i] = [a+a//2 , b+b//2 , arr[i][2]+1]
                victory[i+1] = [c+a*b//(2*d) , d+a*b//(2*c)]
        if len(arr)%2 == 1:
            item = list(arr.items())
            x , y = item[-1][1] , item[-1][0]
            arr = defaultdict(list)
            for i , j in victory.items():
                arr[i] = j
            arr[y] = x
        else:
            for i , j in victory.items():
                arr[i] = j
        for i , j in defeat.items():
                arr[i] = j
for i , j in arr.items():
    print(i+1)
