t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, D = map(int,input().split())     # 꽃의 개수 N, 분무기 범위 D
    garden = [0] * N
    count = 0
    start = D

    while start <N and garden[start] == 0 :
        for i in range(1, D+1) :
            if start - i >= 0 :
                garden[start-i] = 1
            if start + i <= N-1 :
                garden[start+i] = 1
        garden[start] = 1
        start = start + D
        count += 1

    print(count)