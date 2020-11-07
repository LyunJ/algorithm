N, M = input().split()
N = int(N)
M = int(M)

C = input().split()
C = list(map(int, C))

T = list(0 for i in range(N))

one = 0
two = 0
three = 0


def maxelements(lists, checker):
    maxNum = lists[0]
    index = 0
    length = len(lists)
    for i in range(length):
        if lists[i] > maxNum and checker[i] == 0:
            maxNum = lists[i]
            index = i
    return maxNum, index


while True:
    one, one_idx = maxelements(C, T)
    if one >= M:
        T[one_idx] = 1
    else:
        break

while True:
    two, two_idx = maxelements(C, T)
    if one + two >= M:
        T[two_idx] = 2
    else:
        break

while True:
    three, three_idx = maxelements(C, T)
    if one + two + three > M:
        T[three_idx] = 3
    else:
        break


print(one+two+three)