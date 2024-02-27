di = [0, 1]
dj = [1, 0]

def move(st_i, st_j, s) :
    global en_i, en_j
    if st_i == en_i and st_j == en_j :  # 만약 위치가 끝나는 위치라면,
        s += arr[st_i][st_j]            # 끝나는 위치의 값을 더한 후,
        mul_li.append(s)                # 합을 리스트에 추가해준다.
        return

    s += arr[st_i][st_j]                # 자신이 위치한 자리의 숫자를 더해준다.

    for k in range(2) :                 # 오른쪽과 아래쪽으로 가볼거예요
        ni = st_i + di[k]
        nj = st_j + dj[k]
        if 0<=ni<N and 0<=nj<N :        # 만약, 가려는 값이 배열 안에 있다면,
            move(ni, nj, s)             # 재귀함수! 또 실행해준다.
    else :                              # for문을 다 돌았다면,
        return                          # 리턴해준다.



t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())            # NxN 을 위한 길이 N 받기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 받기
    st_i, st_j = 0, 0           # 시작위치와 끝나는 위치를 저장해준다
    en_i, en_j = N-1, N-1
    mul_li = []                 # 경로까지의 합들을 저장할 리스트
    s = 0                       # 경로의 합을 저장하기 위한 변수 생성

    move(st_i,st_j,s)

    min_v = mul_li[0]           # 최소값을 찾아보기 위해 우선 리스트의 맨 첫번째로 설정

    for i in range(len(mul_li)) :       # 리스트를 다 돌면서,
        if min_v > mul_li[i] :          # 지정해둔 최소값보다 작으면,
            min_v = mul_li[i]           # 재할당


    print(f'#{tc} {min_v}')