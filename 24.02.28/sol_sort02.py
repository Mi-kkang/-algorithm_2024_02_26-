arr = [[2,2], [1,3], [1,2], [3,1]]
# [x,y] 좌표들 / y에 대해 오름차순 정렬, y가 같은 경우 x가 작은 순으로
arr.sort()
arr.sort(key=lambda x : x[1])
# arr.sort(key=lambda x : [x[1], x[0]]) 로도 사용 가능
print(arr)