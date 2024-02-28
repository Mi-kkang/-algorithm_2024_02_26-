def ncr(n, r, s) :
    if r == 0 :         # 더이상 고를게 없다면, (다 골랐다면,)
        print(*comb)

    else :
        for i in range(s, n-r+1) :
            comb[r-1] = A[i]
            ncr(n, r-1, i+1)

N = 5
A = [1, 2, 3, 4, 5]
R = 3
comb = [0]*R        # 조합 저장
ncr(N,R,0)