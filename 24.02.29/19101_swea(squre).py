t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    x_s, y_s, x_e, y_e = map(int,input().split())   # 상자 1의 시작점 끝점 받기
    a_s, b_s, a_e, b_e = map(int, input().split())  # 상자 2의 시작점 끝점 받기
    ans = -1

    # 사각형끼리 완전 분리되어 있는 경우 : 4
    if x_e < a_s or x_s > a_e or y_e < b_s or y_s > b_e :
        ans = 4

    else :
        # 점끼리 만나는 경우 : 3
        if (x_s == a_e and y_s == b_e) or (x_e == a_s and y_s == b_e) or (x_e == a_s and y_e == b_s) or (x_s == a_e and y_e == b_s) :
            ans = 3

        # 선끼리 만나는 경우 : 2 // 점의 x, y 좌표가 완전 일치하는 건 앞에서 걸러졌기 때문에, x 혹은 y만 같으면 선으로 겹쳐지는 상황이 된다.
        elif (x_e == a_s) or (x_s == a_e) or (y_s == b_e) or (y_e == b_s) :
            ans = 2

        # 겹치는 경우 : 1
        else:
            ans = 1

    print(f'#{tc} {ans}')