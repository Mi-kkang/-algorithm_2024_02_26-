t = int(input())

for tc in range(1, t+1) :
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    min_v = N*M

    for i in range(N-2) :       # W 영역의 마지막 행
        for j in range(N-1) :   # B 영역의 마지막 행
            cnt = 0             # 각 색으로 바꾸기 위해 칠해야 하는 수
            for p in range(N) :
                for q in range(M) :
                    if p <= i and flag[p][q] != 'W' :
                        cnt += 1

                    elif i < p <= j and flag[p][q] != 'B' :
                        cnt += 1

                    elif j < p and flag[p][q] != 'R' :
                        cnt += 1

            if min_v > cnt :
                min_v = cnt

    print(f'#{tc} {min_v}')