# [도전] 친구와 카페 방문

arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)
ans = 0

def sel_fri(tar) :
    global ans
    cnt = 0
    line = [0] * n
    for i in range(n) :
        if tar & 0x1:
            cnt += 1
            line[i] = 1
        tar >>= 1

    if cnt >= 2 :
        ans += 1
        print('{', end='')
        for j in range(n) :
            if line[j] == 1 :
                print(arr[j], end='')
        print('}')

for tar in range(1<<n) :
    sel_fri(tar)
print(ans)