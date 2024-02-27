def f(i, j, N, s) :     # i,j칸에 진입, s 지나온 칸의 합계
    global min_v
    global cnt
    if i >= N or j >= N :   # 배열을 벗어난 경우,
        return
    elif i == N-1 and j == N-1 :
        if min_v > s + arr[N-1][N-1] :  # 마지막칸을 포함한 합계가 최소인 경우
            min_v = s + arr[N-1][N-1]
        # return 생략

    elif s >= min_v :
        return

    else :
        cnt += 1
        f(i+1, j, N, s+arr[i][j])
        f(i, j+1, N, s+arr[i][j])



t = int(input())

for tc in range(1, t+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 4000
    cnt = 0
    f(0, 0, N, 0)

    print(f'#{tc} {min_v}')