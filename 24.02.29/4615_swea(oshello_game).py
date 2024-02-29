def play_game(i, j, col, N) :   # i : 입력 행, j : 입력 열, col : 입력 색상, N : 전체 보드 길이
    board[i][j] = col           # 해당 위치에 돌의 색을 넣어준다.

    di = [0,1,1,1,0,-1,-1,-1]   # 델타를 설정한다 (상하좌우, 대각선들 모두)
    dj = [1,1,0,-1,-1,-1,0,1]

    for k in range(8) :
        ni = i + di[k]
        nj = j + dj[k]
        change = []         # 돌의 색을 바꿀 좌표를 넣을 리스트 생성

        while 0<=ni<N and 0<=nj<N and board[ni][nj] == 3 - col :   # 범위내에 있고, 색이 다를 때,
            change.append((ni,nj))  # 리스트에 좌표를 넣어준다.
            ni = ni + di[k]         # 좌표를 이동 한다.
            nj = nj + dj[k]

        if 0<=ni<N and 0<=nj<N and board[ni][nj] == col :   # 범위 내에 있고, 색이 같을 때,
            for p, q in change :        # 넣어뒀던 색을 바꿀 좌표를 하나씩 꺼낸다
                board[p][q] = col       # 색을 바꿔준다.



t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # 보드 한 변의 길이 N (NxN), 돌을 놓는 횟수 M
    play = [list(map(int, input().split())) for _ in range(M)]  # (열, 행, 돌의 색) 리스트로 받기
    B = 1   # 흑돌은 1
    W = 2   # 백돌은 2

    board = [[0]*N for _ in range(N)]   # 아무것도 들어가있지 않은 보드판 만들기

    board[N//2-1][N//2-1] = W       # 초기에 놓인 돌들
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W

    for j, i, col in play :
        play_game(i-1, j-1, col, N)
        # i-1, j-1을 하는 이유는 입력값은 1부터 시작이지만, 내가 만든 리스트는 0부터 시작이라서

    cnt_b = 0       # 검은 돌의 개수를 넣을 변수
    cnt_w = 0       # 하얀 돌의 개수를 넣을 변수

    for i in range(N) :             # 보드판을 다 돌면서,
        for j in range(N) :
            if board[i][j] == B :   # 검은색 돌을 발견하면,
                cnt_b += 1          # 검은 돌의 개수를 추가한다.

            elif board[i][j] == W : # 하얀 돌을 발견하면,
                cnt_w += 1          # 하얀 돌의 개수를 추가한다.

    print(f'#{tc} {cnt_b} {cnt_w}')