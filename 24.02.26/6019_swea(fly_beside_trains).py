t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    D, A, B, F = map(int, input().split())      # 두 기차 사이의 거리 D, A기차의 속력, B 기차의 속력, 파리의 속력 F
    T = D * F / (A+B)                         # 시간 = 속력 / 거리

    print(f'#{tc} {T:.10f}')