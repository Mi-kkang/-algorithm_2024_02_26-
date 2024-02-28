# [도전] 주사위 던지기

dice = [1, 2, 3, 4, 5, 6]
N = 3
path = []

def func(lev, start) :
    if lev == N :
        print(path)
        return

    for i in range(start, 7) :
        path.append(i)
        func(lev + 1, i)        # 주사위라 func(lev + 1, i) 이다.
        # 중복이 불가능하면 func(lev+1, i+1)이 된다.
        path.pop()


func(0,1)