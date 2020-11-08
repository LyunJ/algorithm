a, b = map(int, input().split())

D = []
mini = 100000000000

for _ in range(a):
    D.append(list(input()))


for i in range(a-7):
    for j in range(b-7):
        black = 0
        white = 0
        for p in range(i, i+8):
            for q in range(j, j+8):
                if (q + p*8) % 2 == 0:
                    if(p % 2 == 0):
                        if(D[p][q] == 'W'):
                            black += 1
                        else:
                            white += 1

                    else:
                        if(D[p][q] == 'B'):
                            black += 1
                        else:
                            white += 1

                else:
                    if(p % 2 == 0):
                        if(D[p][q] == 'B'):
                            black += 1
                        else:
                            white += 1

                    else:
                        if(D[p][q] == 'W'):
                            black += 1
                        else:
                            white += 1

        if(black < mini):
            mini = black
        if(white < mini):
            mini = white

print(mini)
