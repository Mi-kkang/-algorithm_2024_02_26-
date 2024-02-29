def find_omok(N) :
    global ans
    for i in range(N):              # 오목판을 전부 확인할거야
        for j in range(N):
            if arr[i][j] == 'o':    # 만약 오목알이 있다면,
                # cnt = 1

                for k in range(4):          # 거기서부터 4방향을 확인한다.
                    cnt = 1                 # 개수를 1개로 시작
                    for l in range(1, 5):   # 오목알이 있는 곳부터 4개까지
                        ni = i + di[k] * l
                        nj = j + dj[k] * l

                        # 확인하려는 곳이 오목판 범위 안에 있고, 오목알이 있다면,
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            cnt += 1    # 개수를 1개 늘려준다.
                        # else:
                        #     cnt = 0
                        #     break
                    if cnt == 5:    # 4칸 앞까지 다 확인한 후 오목알이 5개이면
                        ans = True  # 오목 5개!
                        return      # 끝! 리턴!


t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # NxN 크기의 판의 길이 N
    arr = [list(map(str,input())) for _ in range(N)]    # 오목판 받기
    di = [0, 1, 1, -1]      # 4방향을 확인할 델타
    dj = [1, 1, 0, 1]       # 오른쪽, 오른쪽 대각선, 아래, 왼쪽 대각선

    ans = False             # 오목 5개를 확인하기 위한 변수 / False로 초기화
    find_omok(N)

    if ans == True :
        print(f'#{tc} YES')
    else :
        print(f'#{tc} NO')