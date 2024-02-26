t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # 반지름의 길이 N
    count = 0

    for i in range(-N, N+1) :       # 원이라 음수도 확인해줘야 함!
        for j in range(-N, N+1) :
            if (i**2) + (j**2) <= N**2 :
                count += 1

    print(f'#{tc} {count}')