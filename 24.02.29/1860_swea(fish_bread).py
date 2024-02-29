t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M, K = map(int, input().split())     # 손님 N, M초 동안 붕어빵 K개
    customer = list(map(int, input().split()))  # 손님이 오는 시간 받기
    customer.sort()     # 빠른 시간으로 정렬하기
    sale = 0            # 누적 판매 개수
    ans = True          # 바로 판매가 가능한지 확인하기 위한 변수

    for son in customer :
        bread = (son // M) * K      # 손님이 오는 시간에 예상 붕어빵 수
        buy = bread - sale          # 앞에서 사간 붕어빵의 수를 뺀 지금 있는 붕어빵 수

        if buy > 0 :                # 만약 붕어빵이 있다면,
            sale += 1               # 사람이 사갔다! 누적 판매가 하나 증가

        else :                      # 붕어빵이 없다...
            ans = False             # 판매 불가... 브레이크
            break

    if ans :
        print(f'#{tc} Possible')

    else :
        print(f'#{tc} Impossible')