# [도전] 중복 순열과 순열 구현하기
# N개의 주사위를 던져 나올 수 있는 모든 중복순열(Type1)과 순열(Type2)를 출력하시오.

dice = []
visited = [0]*(6+1)

def Type1(x) :
    global n
    if x == n :
        print(dice)
        return

    for i in range(1,7) :
        dice.append(i)
        Type1(x+1)
        dice.pop()

def Type2(x) :
    global n
    if x == n :
        print(dice)
        return

    for i in range(1,7) :
        if visited[i] == 1 :
            continue
        visited[i] = 1
        dice.append(i)
        Type2(x+1)
        dice.pop()
        visited[i] = 0

n, type = map(int, input().split())
if type == 1 :
    Type1(0)
if type == 2 :
    Type2(0)