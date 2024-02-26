t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())    # 자연수 개수 N
    n_li = input().split()    # 리스트 받기

    first = 0
    if N % 2 == 0 :
        second = N // 2
    else :
        second = (N // 2) + 1
    end = second

    suffle = []

    for i in range(N//2) :
        suffle.append(n_li[first])
        first += 1
        suffle.append(n_li[second])
        second += 1

        if first == end :
            if N % 2 == 0 :
                break
            else : 
                suffle.append(n_li[first])
                break

    # while first != end :
    #     suffle.append(n_li[first])
    #     first += 1
    #     suffle.append(n_li[second])
    #     second += 1
    #
    # if second != N-1 :
    #     suffle.append(n_li[N-1])

    print(f'#{tc}', *suffle)