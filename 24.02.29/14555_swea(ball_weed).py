t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    ground = list(input())  # 땅을 리스트로 받는다.
    ball = 0                # 공의 최솟값을 저장할 변수 생성

    for k in range(len(ground)) :   # 땅의 리스트의 길이만큼 반복문을 돈다!
        if ground[k] == '(' :       # 공의 왼쪽이 보인다!
            ball += 1               # 공의 개수 하나 추가
        elif ground[k] == ')' and ground[k-1] != '(' :  # 공의 오른쪽이 보인다! 그런데 전이 공의 왼쪽이 아니었다!
            ball += 1                                   # 공의 개수 하나 추가! (왼쪽이 보이면 전에 추가한거라 배제했음)

    print(f'#{tc} {ball}')