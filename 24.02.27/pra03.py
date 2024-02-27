# branch = 2
# level = 3

def run(level) :

    if level == 3 :
        return

    for i in range(2) :     # 재귀를 몇 번 쓰냐를 결정할 for 문
        run(level + 1)

run(0)