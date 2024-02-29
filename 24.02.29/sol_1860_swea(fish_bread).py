def start() :
    sold_bread = 0
    for person in customers :
        # 공식, 특정시간에 만들 수 있는 빵의 개수
        made_bread = (person // m) * k

        # 빵을 1개 팔았다
        sold_bread += 1

        # 재고 계산
        remain = made_bread - sold_bread

        # 재고가 0보다 작으면 실패 << 0은 성공이다. 왜? 다 팔린거니까! 음수만 아니면 오케이!
        if remain < 0 :
            return 'Impossible'
    return 'Possible'

t = int(input())

for tc in range(1, t+1) :
    # 손님수 n, m초에 k개의 빵을 만든다. 손님들이 도착하는 시간 customers
    n, m, k = map(int,input().split())
    customers = list(map(int, input().split()))
    customers.sort()        # 오름차순 sort

    result = start()

    print(f'#{tc} {result}')