t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())        # 돌의 개수 N, 뒤집기 횟수 M
    arr = list(map(int, input().split()))

    for _ in range(M) :
        st, ad = map(int, input().split())  # 시작 위치 st, st부터 ad개
        st -= 1                             # 인덱스는 0부터 시작이니 하나 빼준다.

        for i in range(st, st+ad) :         # st부터 ad개의 돌까지,
            if i < N :                      # 돌이 범위 내에 있을 때,
                arr[i] = arr[st]            # 시작 돌과 같게 만들어준다.


    print(f'#{tc}', *arr)