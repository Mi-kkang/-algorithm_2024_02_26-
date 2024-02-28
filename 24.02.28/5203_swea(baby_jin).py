def baby_jin(i) :
    global one, two
    if one == 1 :
        return 1

    if two == 1 :
        return 2

    if i % 2 == 0 :     # 카드를 한장 씩 준다. (짝수 인덱스면 1에게 / 홀수면 2에게)
        one_li.append(card[i])
    else :
        two_li.append(card[i])

    if len(one_li) >= 3 :   # 가지고 있는 카드가 3장 이상이면,
        check = [0] * 10    # 카드의 숫자를 저장하자 (카운팅 정렬)
        run1 = 0             # 런 변수 생성
        triplet = 0         # 트리플렛 변수 생성
        for i in one_li :   # 리스트를 돌면서
            check[i] += 1   # 카운팅 리스트에 저장

        for j in range(10) :    # 카운팅 리스트를 확인하기 위해 0~9까지 반복문 돌기
            if check[j] >= 3 :  # 해당 숫자의 개수가 3개 이상이면,
                run1 += 1        # 런이다.
                break           # 런 하나 이상! 탈출!
            elif check[j] >= 1 and j+2 < 10 :               # 해당 숫자가 1개 이상이며, 뒤쪽 두개가 범위 안에 있을 때,
                if check[j+1] >= 1 and check[j+2] >= 1 :    # 해당 숫자, 해당 숫자 + 1, 해당 숫자 + 2 가 모두 1개 이상일 때,
                    triplet += 1                            # 트리플렛이다.
                    break                                   # 트리플렛 하나 이상! 탈출!

        if run1 > 0 or triplet > 0 :     # 런이나 트리플렛이 1개 이상이면,
            return 1                    # 1을 리턴해준다.

    if len(two_li) >= 3:        # 2일때에도 해준다.
        check2 = [0] * 10
        run2 = 0
        triplet2 = 0
        for i in two_li:
            check2[i] += 1

        for j in range(10):
            if check2[j] >= 3:
                run2 += 1
                break
            elif check2[j] >= 1 and j + 2 < 10:
                if check2[j + 1] >= 1 and check2[j + 2] >= 1:
                    triplet2 += 1
                    break

        if run2 > 0 or triplet2 > 0:
            return 2





t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    card = list(map(int, input().split()))
    num = 12        # 숫자 카드의 수 12개 고정
    one = 0         # 첫번째 사람의 성공, 두번째 사람의 성공을 넣어줄 변수 생성
    two = 0         # (( 그런데 하다보니까 필요없는 것 같음 ))
    ans = -1        # 우승한 사람에 따라 값을 넣어줄 변수 생성 // 0이면 무승부, 1이면 1번 사람 승, 2이면 2번 사람 승
    one_li = []     # 1번 사람의 카드를 담을 리스트
    two_li = []     # 2번 사람의 카드를 담을 리스트

    # print(card)

    for i in range(num) :
        ans = baby_jin(i)

        if ans == 1 or ans == 2 :
            break

    if ans != 1 and ans != 2 :
        ans = 0

    print(f'#{tc} {ans}')