def main():
    n , m = map(int , input().split())
    fight = list(map(int , input().split()))
    dg = list(map(int , input().split()))
    id = list(map(int , input().split()))
    times = [0]*n
    while len(id)>1:
        victoryid = []
        defeatid = []
        for i in range(0 , len(id)+1 , 2):
            try:
                pl1 , pl2 = id[i] , id[i+1]
            except IndexError:
                victoryid.append(id[i])
                break
            a , b , c , d = fight[pl1-1] , dg[pl1-1] , fight[pl2-1] , dg[pl2-1]
            if a*b >= c*d:
                times[pl2-1] += 1
                victoryid.append(pl1)
                if times[pl2-1] < m :defeatid.append(pl2)
                fight[pl1-1] , dg[pl1-1] = a+c*d//(2*b) , b+c*d//(2*a)
                fight[pl2-1] , dg[pl2-1] = c+c//2 , d+d//2
            else:
                times[pl1-1] += 1
                victoryid.append(pl2)
                if times[pl1-1] < m :defeatid.append(pl1)
                fight[pl1-1] , dg[pl1-1] = a+a//2 , b+b//2 
                fight[pl2-1] , dg[pl2-1] = c+a*b//(2*d) , d+a*b//(2*c)
        id = victoryid + defeatid
    print(id[0])
main()
