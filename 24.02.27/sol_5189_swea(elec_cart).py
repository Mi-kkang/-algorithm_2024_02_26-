def f1(i,k) :
    global min_v
    if i == k :
        # p 순서로 방문했을 때의 비용
        s = e[0][p[0]-1]    # 사무실에서 첫번째 관리구역
        for j in range(1,k) :
            s += e[p[j-1]-1][p[j]-1]
        s += e[p[k-1]-1][0]

        if min_v > s :
            min_v = s

    else :
        for j in range(k) :
            if used[j] == 0 :
                used[j] = 1
                p[i] = arr[j]
                f1(i+1,k)
                used[j] = 0


t = int(input())

for tc in range(1, t+1) :
    N = int(input())
    e = [list(map(int,input().split())) for _ in range(N)]

    arr = [i for i in range(2, N+1)]
    used = [0]*(N-1)    # 사무실 제외
    p = [0] * (N-1)
    min_v = 10000
    f1(0, N-1)

    print(f'#{tc} {min_v}')