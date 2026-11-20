def ans(command):
    current_side = 10
    count = 0
    start = 0
    document = []
    time = []
    def move(tx):
        nonlocal count , current_side , start
        tx = int(tx)
        count += abs(current_side-tx)
        current_side = tx
        start += 3
    def loop():
        nonlocal count , current_side , start , document , time
        while start < len(command):
            if command[start] == 'T':
                move(str(command[start+1])+str(command[start+2]))
            elif command[start] == 'L':
                time.append(int(command[start+1]))
                document.append(start)
                start += 2
            elif command[start] == 'E':
                if time[-1]-1 == 0:
                    del time[-1],document[-1]
                    start += 1
                else:
                    start = document[-1]+2
                    time[-1] -= 1
    loop()
    return count
if __name__ == '__main__':
    try:
        command = str(input())
        print(ans(command))
    except:
        exit()
