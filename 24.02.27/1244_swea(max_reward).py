def make_money(i,n, change) :
    global max_v
    if i == int(change) :       # 바꾼 횟수가 바꿀 수 있는 횟수와 같을 경우,
        money = 0               # 금액을 저장하기 위한 변수 생성
        money = int(''.join(reword))
        # for k in range(n) :     # 리스트 인덱스를 모두 돌 예정
        #     money += int(reword[k]) * (10 ** (n-1-k))   # 각 자리수에 따라 10** 해주기
        # # print(money)
        if max_v < money :      # 나온 금액이 최대값보다 크다면,
            max_v = money       # 재할당
        return

    else :
        for j in range(n) :
            for l in range(n) :
                if j != l :
                    reword[j], reword[l] = reword[l], reword[j]  # 바꾸자
                    # print(int(''.join(reword)))
                    if max_v < int(''.join(reword)) :
                        make_money(i+1, n, change)                  # 재귀 ㄱㄱ
                    reword[j], reword[l] = reword[l], reword[j] # 원상복구

        # for j in range(i, n) :     # 자리를 바꿔보아요
        #     reword[i], reword[j] = reword[j], reword[i] # 바꾸자
        #     # print(reword)
        #     make_money(i+1, n, change)                  # 재귀 ㄱㄱ
        #     reword[i], reword[j] = reword[j], reword[i] # 원상복구


t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    reword, change = input().split()            # 숫자판 reword / 변경 횟수 change
    reword = list(reword)                       # 숫자판을 리스트화
    N = len(reword)                             # 숫자판 길이(숫자 개수) N
    max_v = 0                                   # 최대 상금을 저장할 변수 생성
    # bit = [i for i in range(N)]
    make_money(0,N, change)

    print(f'#{tc} {max_v}')