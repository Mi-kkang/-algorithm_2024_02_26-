t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # 돌아가야 할 학생 수 N
    back = []               # 학생들 이동할 경로를 담을 리스트 생성

    for _ in range(N) :
        route = list(map(int,input().split()))
        route.sort()

        for i in range(len(route)) :
            if route[i] % 2 == 0 :
                route[i] -= 1

        back.append((route[0], route[1]))

    