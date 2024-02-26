t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # 전선의 개수 N
    a = []
    b = []
    cnt = 0

    for i in range(N) :
        st, en = map(int, input().split())
        a.append(st)
        b.append(en)

    for j in range(N) :
        for k in range(j, N) :
            if j+k < N-1 :
                if a[j] < a[j+k] and b[j] > b[j+k] :
                    cnt += 1

                elif a[j] > a[j+k] and b[j] < b[j+k] :
                    cnt += 1

    print(f'#{tc} {cnt}')