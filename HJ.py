import numpy as np

D = np.zeros((100, 100, 100, 3, 4))
E = np.zeros((100, 100, 100, 3, 4))


def sex(a, b, c, myTurn, can):
    if(a == 0 and b == 0 and c == 0):
        return True if myTurn else False
    if(a == 1 and b == 0 and c == 0):
        return False if myTurn else True
    if(a == 0 and b == 1 and c == 0):
        return False if myTurn else True
    if(a == 0 and b == 0 and c == 1):
        return False if myTurn else True
    if(a == 1 and b == 1 and c == 0):
        return True if myTurn else False
    if(a == 0 and b == 1 and c == 1):
        return True if myTurn else False
    if(a == 1 and b == 0 and c == 1):
        return True if myTurn else False
    if(a == 1 and b == 1 and c == 1):
        return False if myTurn else True

    if(len(can) == 3):
        if(a-can[0] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[0])
            r1 = sex(a-can[0], b, c, not myTurn, can_input)
        else:
            r1 = False
        if(a-can[1] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[1])
            r2 = sex(a-can[1], b, c, not myTurn, can_input)
        else:
            r2 = False
        if(a-can[2] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[2])
            r3 = sex(a-can[2], b, c, not myTurn, can_input)
        else:
            r3 = False
        if(b-can[0] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[0])
            r4 = sex(a, b-can[0], c, not myTurn, can_input)
        else:
            r4 = False
        if(b-can[1] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[1])
            r5 = sex(a, b-can[1], c, not myTurn, can_input)
        else:
            r5 = False
        if(b-can[2] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[2])
            r6 = sex(a, b-can[2], c, not myTurn, can_input)
        else:
            r6 = False
        if(c-can[0] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[0])
            r7 = sex(a, b, c-can[0], not myTurn, can_input)
        else:
            r7 = False
        if(c-can[1] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[1])
            r8 = sex(a, b, c-can[1], not myTurn, can_input)
        else:
            r8 = False
        if(c-can[2] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[2])
            r9 = sex(a, b, c-can[2], not myTurn, can_input)
        else:
            r9 = False
        return r1 or r2 or r3 or r4 or r5 or r6 or r7 or r8 or r9
    else:
        if(myTurn == True and (D[a][b][c][can[0]][can[1]] == -1 or D[a][b][c][can[0]][can[1]] == 1)):
            return True if D[a][b][c][can[0]][can[1]] == 1 else False
        if(myTurn == False and (E[a][b][c][can[0]][can[1]] == -1 or E[a][b][c][can[0]][can[1]] == 1)):
            return True if E[a][b][c][can[0]][can[1]] == 1 else False
        if(a-can[0] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[0])
            r1 = sex(a-can[0], b, c, not myTurn, can_input)
        else:
            if(myTurn == True):
                r1 = False
            else:
                r1 = True
        if(a-can[1] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[1])
            r2 = sex(a-can[1], b, c, not myTurn, can_input)
        else:
            if(myTurn == True):
                r2 = False
            else:
                r2 = True
        if(b-can[0] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[0])
            r3 = sex(a, b-can[0], c, not myTurn, can_input)
        else:
            if(myTurn == True):
                r3 = False
            else:
                r3 = True
        if(b-can[1] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[1])
            r4 = sex(a, b-can[1], c, not myTurn, can_input)
        else:
            if(myTurn == True):
                r4 = False
            else:
                r4 = True
        if(c-can[0] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[0])
            r5 = sex(a, b, c-can[0], not myTurn, can_input)
        else:
            if(myTurn == True):
                r5 = False
            else:
                r5 = True
        if(c-can[1] >= 0):
            can_input = [1, 2, 3]
            can_input.remove(can[1])
            r6 = sex(a, b, c-can[1], not myTurn, can_input)
        else:
            if(myTurn == True):
                r6 = False
            else:
                r6 = True

        if (myTurn == True):
            D[a][b][c][can[0]][can[1]] = 1 if (
                r1 or r2 or r3 or r4 or r5 or r6) else -1
            return r1 or r2 or r3 or r4 or r5 or r6
        else:
            E[a][b][c][can[0]][can[1]] = 1 if (
                r1 and r2 and r3 and r4 and r5 and r6) else -1
            return r1 and r2 and r3 and r4 and r5 and r6


n = int(input())
for i in range(n):
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    can = [1, 2, 3]
    myTurn = True
    result = sex(A, B, C, myTurn, can)
    print(result)
