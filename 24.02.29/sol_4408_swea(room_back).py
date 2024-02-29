t = int(input())

for tc in range(1, t+1) :
    N = int(input())
    # 복도 리스트 초기화
    corridor = [0] * 400
    max_v = 0

    for _ in range(N) :
        # 현재방 s, 돌아갈 방 e
        s, e = map(int,input().split())

        # 특징 2번 아랫방을 윗방으로 변경
        if s % 2 == 0 :
            s -= 1
        if e % 2 == 0 :
            e -= 1

        # 특징 1번 : 출발지보다 목적지가 더 큰 값이 되도록 swap
        if s > e :
            s, e = e, s

        for i in range(s, e+1) :                # 출발지와 목적지를 돌면서
            corridor[i] += 1                    # 해당 위치에 1을 추가해준다.
            max_v = max(corridor[i], max_v)     # 최대값과 비교해 더 큰 걸 다시 저장해준다.

    print(f'#{tc} {max_v}')