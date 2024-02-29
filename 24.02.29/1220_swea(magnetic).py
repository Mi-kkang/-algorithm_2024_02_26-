t = 10                      # 테스트 케이스 10개 고정

for tc in range(1, t+1) :
    N = int(input())        # 테이블 크기 받기 (항상 100이긴 하다)
    arr = [list(map(int, input().split())) for _ in range(N)]
    # red = False           # 여기서 하면 열을 돌 때마다 초기화가 안 된다!! 여기 아님!!!
    cnt = 0

    for j in range(N) :         # 열을 돌아볼 예정입니당
        red = False             # N극을 확인할 변수 생성
        for i in range(N) :
            if arr[i][j] == 1 : # 만약 N극이라면,
                red = True      # N극에 True 해줌

            elif red == True and arr[i][j] == 2 :       # N극이 이전에 있었고, S극을 만났으면,
                cnt += 1                                # 교착상태 하나 추가!
                red = False                             # 다시 N극 False 해줌



    print(f'#{tc} {cnt}')