# [도전] 중복순열 [1,1,1]~[6,6,6] 까지 출력하는 코드를 재귀호출로 구현하자

path = []

def per(x) :
    if x == 3 :
        print(path)
        return

    for i in range(1,7) :
        path.append(i)
        per(x+1)
        path.pop()

def per2(x) :
    if x == 5 :
        print(path)
        # path.pop()    도 가능
        return

    for i in range(1, 5) :
        path.append(i)
        per2(x+1)
        path.pop()  # 여기 pop은 이쪽 말고 x == 5 : 부분에서 return 직전에 넣어도 괜찮다.


# per(0)
per2(0)