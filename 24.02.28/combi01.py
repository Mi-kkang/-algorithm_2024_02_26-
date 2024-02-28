# N개에서 2개를 고르는 조합
N = 5

for i in range(N-1) :           # i : 0 -> N-2
    for j in range(i+1, N) :
        print(i,j)
        # if arr[i] + arr[j] <= M and max_v < arr[i] + arr[j]   # <- 한빈이와 spot mart 힌트


# n개에서 r개를 고르는 조합(재귀)
def nCr(n, r, s) : # n개에서 r개를 고르는 조합. s : 선택할 수 있는 구간의 시작
    if r == 0 :
        print(*comb)

    else :
        for i in range(s,n-r+1) :
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)