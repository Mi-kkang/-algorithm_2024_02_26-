t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    x_s, y_s, x_e, y_e = map(int,input().split())   # 상자 1의 시작점 끝점 받기
    a_S, b_s, a_e, b_e = map(int, input().split())  # 상자 2의 시작점 끝점 받기

    