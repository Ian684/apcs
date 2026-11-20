from collections import defaultdict
def main():
    m = int(input())
    arr = defaultdict(set)
    result = 0
    for i in range(m):
        a = input()
        arr[len(a)].add(a)
    for i in range(1,101):
        if i in arr:
            for j in arr[i]:
                for l in range(1 , (i-1)//2+1):
                    if j[0:l] == j[i-l:i]:
                        middle = j[l:i-l]
                        if middle in arr[len(middle)]:
                            result+=1
    print(result)
main()
