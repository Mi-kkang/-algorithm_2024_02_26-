def find_sudoku(N) :
    # 정상적인 스도쿠인지 아닌지를 확인해볼 예정이다.
    global ans

    # 1. 가로를 확인할 것이다.
    for i in range(N) :
        num = []    # 숫자를 넣을 리스트
        for j in range(N) :
            if sudoku[i][j] in num :    # 리스트에 들어있는 숫자라면,
                ans = 0                 # 정상적인 스도쿠가 아니다!
                return                  # 리턴!
            elif sudoku[i][j] not in num :
                num.append(sudoku[i][j])

    # 2. 세로를 확인할 것이다.
    for j in range(N) :
        num = []
        for i in range(N) :
            if sudoku[i][j] in num :
                ans = 0
                return
            else :
                num.append(sudoku[i][j])

    # 3. 3x3 크기의 격자를 확인해 볼 예정이다.
    for k in range(3) :
        st = 3*k    # 격자의 시작점을 결정하기 위한 변수 (0, 3, 6)
        num = []
        for i in range(st, st+3) :
            for j in range(st, st+3) :
                if sudoku[i][j] in num :
                    ans = 0
                    return
                else :
                    num.append(sudoku[i][j])








t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = 9                   # 스도쿠 퍼즐을 만들기 위한 길이 N (9로 고정)
    sudoku = [list(map(int,input().split())) for _ in range(N)]     # 스도쿠를 받는다.
    ans = 1     # 이게 정상적인 스도쿠인지 아닌지를 확인하기 위한 변수 / 일단 맞다는 가정을 한다.

    find_sudoku(N)

    print(f'#{tc} {ans}')