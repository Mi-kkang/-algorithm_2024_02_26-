t = int(input())

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # N 컨테이너 수, M 트럭 수
    box = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 크기별로 내림차순 정렬
    box.sort(reverse=True)
    truck.sort(reverse=True)
    total = 0
    while box and truck :       # 컨테이너와 트럭 모두 남아있으면
        if box[0] <= truck[0] : # 가장 큰 트럭이 가장 큰 컨테이너를 옮길 수 있으면,
            total += box.pop(0)
            truck.pop(0)
        else :  # 옮길 수 없으면,
            box.pop(0)  # 무거운 화물 하나 포기

    print(f'#{tc} {total}')