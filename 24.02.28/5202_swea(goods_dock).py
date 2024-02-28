t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # 신청서 개수 N
    apply = []              # 신청서를 담을 리스트
    cnt = 0                 # 신청을 받을 수 있는 개수를 담을 변수
    en_t = 0                # 현재 신청서의 완료시간을 저장할 변수

    for _ in range(N) :                         # 신청서 개수만큼 반복문
        st, en = map(int,input().split())       # 시작시간 st, 완료시간 en << 신청서이다.
        apply.append((st,en))                   # 시작시간과 완료시간을 튜플로 해서 추가해준다.

    apply.sort(key= lambda x : [x[1], x[0]])    # 완료시간을 기준으로 재정렬 / 완료시간이 같다면, 시작시간이 빠른게 앞으로

    for time in apply :             # 정렬한 신청서들을 하나씩 살펴볼 예정입니당
        if time[0] >= en_t :        # 만약 현재 사용하고 있는 사용자의 완료시간보다 시작시간이 뒤쪽이라면, 예약 가능
            cnt += 1                # 받을 수 있으니 신청 개수 하나 증가
            en_t = time[1]          # 그 사용자의 끝나는 시간으로 다시 할당해준다.


    print(f'#{tc} {cnt}')