t = int(input())        # 테스트 케이스 개수 받기

def get_res() :
    a = 0
    b = (len(n_li) + 1) // 2

    for turn in range(len(n_li)) :
        if turn % 2 == 0 :
            print(n_li[a], end=' ')
            a += 1
        else :
            print(n_li[b], end=' ')
            b += 1

for tc in range(1, t+1) :
    N = int(input())    # 자연수 개수 N
    n_li = input().split()    # 리스트 받기

    print(f'#{tc}', end= ' ')
    get_res()
    print()