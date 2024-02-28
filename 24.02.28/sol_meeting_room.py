'''
10
1 4  1 6  6 10  5 7  3 8  5 9  3 5  8 11  2 13  12 14

'''

N = int(input())        # 회의 개수
arr = list(map(int, input().split()))
meeting = []

for i in range(N) :
    si, fi = arr[i*2], arr[(i*2)+1]
    meeting.append((si, fi))
# 종료시간 기준으로 오름차순 정렬...
meeting.sort(key= lambda x : x[1])
cnt = 0     # 배정한 회의 수
fi = 0      # 진행중인 회의의 종료시간
room = []

for i in range(N) :     # i번 회의에 대해
    # i번 회의를 선택하려면, si >= fi 현재 진행중인 회의 이후에 시작
    if meeting[i][0] >= fi :
        cnt += 1
        fi = meeting[i][1]  # 새 회의 종료시간
        room.append((meeting[i][0], meeting[i][1]))

print(cnt)
print(room)