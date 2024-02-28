# 그리디 (화장실 문제)

N = 4
people = [15, 30, 50, 10]

wait = 0

while len(people) > 1 :
    min_t = people[0]
    num = 0
    for i in range(len(people)) :
        if min_t > people[i] :
            min_t = people[i]
            num = i

    time = people.pop(num)
    wait += time * len(people)
    # print(wait)

print(wait)