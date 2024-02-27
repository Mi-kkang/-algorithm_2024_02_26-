def bettery(i,n,v) :
    global min_v
    if i == n :
        if min_v > v :
            min_v = v
    elif v > min_v :
        return

    for j in range(i, n) :
        bit[i], bit[j] = bit[j], bit[i]
        if i == bit[i] :
            bit[i], bit[j] = bit[j], bit[i]
            continue
        else:
            bettery(i+1,n,v + arr[i][bit[i]])
            bit[i], bit[j] = bit[j], bit[i]


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # NxN 배열의 길이 N
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 받기
    bit = [i for i in range(N)]
    s = 0
    min_v = 10001
    v = 0

    bettery(s,N,v)

    print(f'#{tc} {min_v}')