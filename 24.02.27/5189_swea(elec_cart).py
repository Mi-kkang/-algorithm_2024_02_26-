def make_line(s,n) :
    if s == n :                     # 모든 순서를 다 정했으면,
        c = [0] + line[:] + [0]     # 사무실에서 시작해서 끝내야 하니 앞뒤로 사무실 번호[0]을 추가
        # 여기서 중요한건 얕은 복사가 되지 않도록!! 꼭 따로 복사해두어야 한다. (안하면 빈칸으로 생김)
        all.append(c)               # 리스트를 추가해준다.
        return

    else :
        for j in range(s,n) :                   # 위치 순서를 고르자
            bit[s], bit[j] = bit[j], bit[s]     # 바꾸자
            line.append(bit[s])                 # 바꾼 순서를 추가해주자
            make_line(s+1, n)                   # 재귀하자
            bit[s], bit[j] = bit[j], bit[s]     # 다 끝냈으면 다시 원래대로 바꾸자
            line.pop()                          # 바꿨으니 추가했던걸 빼주자



t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # NxN 배열의 길이 N
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 받기
    bit = [i for i in range(1, N)]      # 순번을 정해본다(이때, 맨 앞은 사무실이라 빼고 생성)
    n = N-1     # 사무실을 뺀 N의 길이(N-1)
    line = []   # 사무실을 제외한 순번을 넣어둘 리스트
    all = []    # 순번들의 리스트를 넣어둘 리스트
    s = 0       # 시작점
    min_v = 10001   # 최소를 정해둔다(제일 커도 10000이 나와서 10001으로 정함)

    make_line(s,n)

    cnt = len(all)  # 리스트를 넣어둔 리스트의 길이를 변수에 할당해주자(반복문을 돌리기 위해)

    for i in range(cnt) :   # 순번들의 리스트를 하나씩 살펴보기 위해 하는 반복문
        score = 0
        for j in range(N) : # 왜 N번만 돌리냐? 리스트 안에 리스가 N+1개이나, 본인과 본인 뒤에 것을 쓸 예정이라 N까지만 확인한다.
            score += arr[all[i][j]][all[i][j+1]]    # 리스트 안에 있는 두 숫자를 각각 배열의 행과 열에 넣어준다.
            # j번 에서 j+1번까지 가는데 필요한 연료를 확인하기 위함 // 이걸 score에 저장해준다.

        if min_v > score :  # 최소와 비교해서 더 작으면,
            min_v = score   # 재할당해준다.

    print(f'#{tc} {min_v}')