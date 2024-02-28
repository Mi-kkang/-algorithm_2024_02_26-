t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int,input().split())             # 컨테이너 수 N, 트럭 수 M
    contain = list(map(int,input().split()))    # 컨테이너 무게 담은 리스트
    track = list(map(int, input().split()))     # 트럭의 최대용량을 담은 리스트
    c_num = len(contain)                        # 컨테이너의 길이(개수) 변수에 저장
    check = [0] * c_num                         # 이미 담아간 컨테이너인지 확인하기 위해 만든 리스트
    cnt = 0                                     # 컨테이너 무게를 저장할 변수

    contain.sort(reverse=True)                  # 컨테이너는 내림차순으로 저장(큰 수가 앞으로)
    track.sort()                                # 트럭은 오름차순으로 저장

    for tr in track :                                   # 트럭 리스트를 다 돌면서,
        for i in range(c_num) :                         # 컨테이너 개수만큼 반복문을 돈다
            if tr >= contain[i] and check[i] == 0 :     # 만약 트럭의 무게보다 작거나 같고, 가져가지 않은 컨테이너라면,
                cnt += contain[i]                       # 냉큼 가져간다
                check[i] = 1                            # 가져갔다고 체크한다
                break                                   # 가져갔으니 트럭은 떠났다. 반복문 탈추울~!!

            # elif tr < contain[i] :
            #     for j in range(i-1, -1, -1) :
            #         if check[j] == 0 :
            #             cnt += contain[j]
            #             check[j] = 1
            #             break

    print(f'#{tc} {cnt}')
