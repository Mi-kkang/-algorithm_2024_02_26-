t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())        # N : 과자수, M : 제한 무게
    arr = list(map(int, input().split()))   # 과자들의 무게 리스트

    max_v = -1   # M을 초과하지 않는 최대합

    for i in range(N-1) :           # 왼쪽 과자
        for j in range(i+1, N) :      # 오른쪽 과자
            if arr[i] + arr[j] <= M and max_v < arr[i] + arr[j] :
                max_v = arr[i] + arr[j]

    print(f'#{tc} {max_v}')