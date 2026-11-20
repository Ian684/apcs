def main():
    first = int(input())
    n = int(input())
    nrr = list(map(int , input().split()))
    last1 = -1
    last2 = -1
    result = ''
    for i in range(len(nrr)):
        if last1 == -1:
            result = rest(nrr[i] , first)
            print(first,end=' ')
            last1 = nrr[i]
        elif last2 ==-1:
            result = rest(nrr[i] , last1)
            print(last1,end=' ')
            last2 = last1
            last1 = nrr[i]
        else:
            if last1 == last2:
                if last1 == 0:
                    result = rest(nrr[i] , 5)
                    print(5 , end=' ')
                elif last1 == 2:
                    result = rest(nrr[i] , 0)
                    print(0 , end=' ')
                else:
                    result = rest(nrr[i] , 2)
                    print(2 , end=' ')
            else:
                result = rest(nrr[i] , last1)
                print(last1 , end=' ')
            last2 = last1
            last1 = nrr[i]
        if result == 'Won' or result == 'Lost':
            print(f': {result} at round {i+1}')
            break
        elif i == n-1 and result == '':
            print(f': Drew at round {i+1}')
            break
def rest(g , b):
    if g == b:
        return ''
    elif g == 0 and b == 2 or g == 2 and b == 5 or g == 5 and b ==0:
        return 'Lost'
    else:
        return 'Won'
main()