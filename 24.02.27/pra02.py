# [도전] 무한 재귀호출

# def KFC(x) :
#     KFC(x+1)
#
#
# KFC(0)
# print('끝')

def KFC(x) :
    if x == 6 :
        return

    print(x, end=' ')
    KFC(x+1)
    print(x, end=' ')


KFC(0)
print()
print('끝')