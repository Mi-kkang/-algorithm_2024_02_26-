def f1(i,k, bat) :  # i : i번째로 방문한 관리구역 결정단계 / bat : 지나온 경로의 소비 배터리양
    global min_v
    if i == k :
        bat += e[p[k-1]][0]
        if min_v > bat :
            min_v = bat

    elif min_v <= bat :
        return

    else :
        for j in range(k) :
            if used[j] == 0 :
                used[j] = 1
                p[i] = j        # arr[j]에 j가 들어있음
                f1(i+1,k, bat + e[p[i-1]][p[i]])
                used[j] = 0


t = int(input())

for tc in range(1, t+1) :
    N = int(input())
    e = [list(map(int,input().split())) for _ in range(N)]
    min_v = 10000
    # arr = [i for i in range(0, N)]  # 사무실 0, 관리구역 1 ~ N-1
    used = [0]*(N)      # 사무실 제외
    p = [0] * (N)       # 0에서 N-1번까지인 순열
    p[0] = 0            # 맨 앞자리는 0로 고정
    used[0] = 1
    bat = 0

    f1(1, N, bat)

    print(f'#{tc} {min_v}')