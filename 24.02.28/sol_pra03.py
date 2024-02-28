# 그리디 (화장실 문제)

person = [15, 30, 50, 10]
n = len(person)
person.sort()
sum = 0
left_person = n - 1 # 화장실을 이용 아직 못한 대기자의 수

for turn in range(n) :
    time = person[turn]
    # 누적합 += 남은사람 * 시간
    sum += left_person * time
    left_person -= 1
print(sum)