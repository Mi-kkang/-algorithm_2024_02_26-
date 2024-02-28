t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # 돌의 개수 N, 바꾸기 횟수 M
    arr = list(map(int, input().split()))

    for _ in range(M) :                 # 바꾸기 횟수만큼 반복해준다.
        i, j = map(int,input().split()) # i번째 돌을 사이에 두고 마주보는 j개의 돌
        i -= 1                          # 인덱스는 0부터 시작하니 1을 빼준다.

        for k in range(1, j+1) :            # i번쨰 돌을 사이에 두고 마주보는 j개의 돌을 찾을 반복문
            if 0<= i-k<N and 0<= i+k<N :    # 만약 마주보는 돌들이 범위 안에 있을 때,
                if arr[i-k] == arr[i+k] :   # 그 돌들이 같은 색일 때,
                    if arr[i-k] == 0 :      # 색을 바꿔준다.
                        arr[i-k] = 1
                        arr[i+k] = 1
                    else :
                        arr[i-k] = 0
                        arr[i+k] = 0

    print(f'#{tc}', *arr)